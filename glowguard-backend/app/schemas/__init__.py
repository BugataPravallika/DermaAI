"""Pydantic schemas for request/response validation"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")  # Basic email validation
    username: str
    full_name: Optional[str] = None
    age: Optional[int] = None
    skin_type: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    age: Optional[int] = None
    skin_type: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool
    
    class Config:
        from_attributes = True

# Prediction Schemas
class PredictionBase(BaseModel):
    disease_name: str
    confidence: float
    severity: str
    description: str
    causes: str

class PredictionCreate(PredictionBase):
    image_path: str

class PredictionResponse(PredictionBase):
    id: int
    user_id: Optional[int] = None
    image_path: str
    timestamp: datetime
    
    class Config:
        from_attributes = True

# Recommendation Schemas
class RecommendationBase(BaseModel):
    category: str  # remedies, products, diet, precautions
    content: str

class RecommendationResponse(RecommendationBase):
    id: int
    prediction_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Product Schemas
class ProductBase(BaseModel):
    name: str
    category: str
    brand: str
    price_range: str
    description: str
    image_url: Optional[str] = None
    purchase_link: Optional[str] = None
    recommended_for: str

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Analysis Result Schemas
class SkinAnalysisResult(BaseModel):
    disease_name: str
    confidence: float
    severity: str
    description: str
    causes: List[str]
    remedies: List[str]
    precautions: List[str]
    diet_advice: dict
    products: List[ProductResponse]

class AnalysisCombinedResponse(BaseModel):
    prediction: PredictionResponse
    analysis: SkinAnalysisResult
    recommendations: List[RecommendationResponse]

# Auth Schemas
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class LoginRequest(BaseModel):
    email: str
    password: str
