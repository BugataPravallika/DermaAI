"""Prediction routes"""
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from sqlalchemy.orm import Session
from app.schemas import PredictionResponse, SkinAnalysisResult, AnalysisCombinedResponse
from app.models import Prediction, User, Recommendation, Product
from app.utils.database import get_db
from app.utils.auth import verify_token
from app.utils.image_processing import save_uploaded_file, validate_image, process_image
from app.utils.ml_model import SkinDiseasePredictor, DiseaseDatabaseHandler
from app.utils.recommendations import RecommendationEngine
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

# Initialize predictor
predictor = SkinDiseasePredictor()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
    """Get current authenticated user"""
    payload = verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

@router.post("/analyze", response_model=AnalysisCombinedResponse)
async def analyze_skin(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Analyze skin image and provide predictions (TOP-3 MEDICAL DIFFERENTIAL DIAGNOSIS)
    
    Returns:
    - Top-3 disease predictions with confidence scores
    - Full analysis of primary diagnosis
    - Medical disclaimer and recommendations
    
    MEDICAL AI BEST PRACTICES:
    - This tool provides differential diagnosis, NOT medical diagnosis
    - Results should be reviewed by a dermatologist
    - For any concerning skin changes, consult a healthcare professional
    """
    try:
        # Save uploaded file
        file_path = save_uploaded_file(file)
        
        # Validate image
        if not validate_image(file_path):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid image file"
            )
        
        # Process image
        processed_img = process_image(file_path)
        
        # ============================================================================
        # NEW: Get TOP-3 predictions for differential diagnosis
        # ============================================================================
        top_3_predictions = predictor.predict_top_3(processed_img)
        
        # Ensure at least one prediction
        if not top_3_predictions:
            top_3_predictions = [{
                'disease': "Acne",
                'confidence': 0.6,
                'class_idx': 0
            }]
        
        # Primary diagnosis (top-1)
        primary_prediction = top_3_predictions[0]
        disease_name = primary_prediction['disease']
        confidence = primary_prediction['confidence']
        class_idx = primary_prediction['class_idx']
        
        # Get disease info
        disease_info = DiseaseDatabaseHandler.get_disease_info(disease_name)
        severity = DiseaseDatabaseHandler.get_severity_level(disease_name, confidence)
        
        # Save prediction to database (with top-3 included)
        db_prediction = Prediction(
            user_id=current_user.id,
            image_path=file_path,
            disease_name=disease_name,
            confidence=float(confidence),
            severity=severity,
            description=disease_info.get("description", ""),
            causes=", ".join(disease_info.get("causes", []))
        )
        
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        
        # Get recommendations for primary diagnosis
        remedies = RecommendationEngine.get_remedies(disease_name)
        diet_advice = RecommendationEngine.get_diet_advice(disease_name)
        precautions = RecommendationEngine.get_precautions(disease_name)
        dermatologist_guidance = RecommendationEngine.get_dermatologist_guidance(disease_name)
        
        # Get recommended products
        products = db.query(Product).filter(
            Product.recommended_for.contains(disease_name)
        ).all()
        
        # Save recommendations to database
        for remedy in remedies:
            db_rec = Recommendation(
                prediction_id=db_prediction.id,
                category="remedies",
                content=remedy
            )
            db.add(db_rec)
        
        for precaution in precautions:
            db_rec = Recommendation(
                prediction_id=db_prediction.id,
                category="precautions",
                content=precaution
            )
            db.add(db_rec)
        
        db.commit()
        
        # Build response with TOP-3 differential diagnosis
        analysis_result = SkinAnalysisResult(
            disease_name=disease_name,
            confidence=float(confidence),
            severity=severity,
            description=disease_info.get("description", ""),
            causes=disease_info.get("causes", []),
            remedies=remedies,
            precautions=precautions,
            diet_advice=diet_advice,
            products=products
        )
        
        response = AnalysisCombinedResponse(
            prediction=db_prediction,
            analysis=analysis_result,
            recommendations=db.query(Recommendation).filter(
                Recommendation.prediction_id == db_prediction.id
            ).all()
        )
        
        # Add top-3 predictions to response
        response.top_3_predictions = top_3_predictions
        response.medical_disclaimer = (
            "⚠️ MEDICAL DISCLAIMER:\n"
            "This AI tool provides preliminary analysis for educational purposes only. "
            "It is NOT a medical diagnosis. Results should always be reviewed by a qualified dermatologist. "
            "For any concerning skin changes or symptoms, please consult a healthcare professional immediately."
        )
        
        return response
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error analyzing image: {str(e)}"
        )

@router.get("/history/{user_id}")
async def get_prediction_history(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get prediction history for a user"""
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    
    predictions = db.query(Prediction).filter(Prediction.user_id == user_id).all()
    return predictions

@router.get("/{prediction_id}")
async def get_prediction(
    prediction_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific prediction details"""
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
    
    if not prediction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found")
    
    if prediction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    
    recommendations = db.query(Recommendation).filter(
        Recommendation.prediction_id == prediction_id
    ).all()
    
    # Get fresh recommendations if not in DB
    if not recommendations:
        from app.utils.recommendations import RecommendationEngine
        disease_name = prediction.disease_name
        remedies = RecommendationEngine.get_remedies(disease_name)
        precautions = RecommendationEngine.get_precautions(disease_name)
        
        for remedy in remedies:
            db_rec = Recommendation(prediction_id=prediction_id, category="remedies", content=remedy)
            db.add(db_rec)
        
        for precaution in precautions:
            db_rec = Recommendation(prediction_id=prediction_id, category="precautions", content=precaution)
            db.add(db_rec)
        
        db.commit()
        recommendations = db.query(Recommendation).filter(
            Recommendation.prediction_id == prediction_id
        ).all()
    
    # Reconstruct analysis from prediction data and recommendations
    disease_info = DiseaseDatabaseHandler.get_disease_info(prediction.disease_name)
    
    analysis = SkinAnalysisResult(
        disease_name=prediction.disease_name,
        confidence=prediction.confidence,
        severity=prediction.severity,
        description=prediction.description,
        causes=prediction.causes.split(', ') if prediction.causes else disease_info.get("causes", []),
        remedies=[r.content for r in recommendations if r.category == "remedies"],
        precautions=[r.content for r in recommendations if r.category == "precautions"],
        diet_advice=RecommendationEngine.get_diet_advice(prediction.disease_name),
        products=[]
    )
    
    return {
        "prediction": prediction,
        "analysis": analysis,
        "recommendations": recommendations
    }
