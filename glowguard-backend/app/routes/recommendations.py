"""Recommendations routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Recommendation
from app.utils.database import get_db

router = APIRouter()

@router.get("/by-prediction/{prediction_id}")
async def get_recommendations_by_prediction(
    prediction_id: int,
    db: Session = Depends(get_db)
):
    """Get recommendations for a specific prediction"""
    recommendations = db.query(Recommendation).filter(
        Recommendation.prediction_id == prediction_id
    ).all()
    
    # Group by category
    result = {}
    for rec in recommendations:
        if rec.category not in result:
            result[rec.category] = []
        result[rec.category].append(rec.content)
    
    return result

@router.get("/by-category/{category}")
async def get_recommendations_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    """Get all recommendations by category"""
    recommendations = db.query(Recommendation).filter(
        Recommendation.category == category
    ).all()
    
    return [{"id": r.id, "content": r.content} for r in recommendations]
