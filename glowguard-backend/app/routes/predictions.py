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
    Analyze skin image and provide predictions
    
    Returns:
    - Disease prediction with confidence
    - Recommendations (remedies, products, diet, precautions)
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
        
        # Get prediction
        disease_name, confidence, class_idx = predictor.predict(processed_img)
        
        # Get disease info
        disease_info = DiseaseDatabaseHandler.get_disease_info(disease_name)
        severity = DiseaseDatabaseHandler.get_severity_level(disease_name, confidence)
        
        # Save prediction to database
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
        
        # Get recommendations
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
        
        # Build response
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
        
        return AnalysisCombinedResponse(
            prediction=db_prediction,
            analysis=analysis_result,
            recommendations=db.query(Recommendation).filter(
                Recommendation.prediction_id == db_prediction.id
            ).all()
        )
    
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
    
    return {
        "prediction": prediction,
        "recommendations": recommendations
    }
