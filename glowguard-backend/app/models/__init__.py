"""Database models for GlowGuard"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    age = Column(Integer, nullable=True)
    skin_type = Column(String, nullable=True)  # oily, dry, combination, normal
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    image_path = Column(String)
    disease_name = Column(String)
    confidence = Column(Float)
    severity = Column(String)  # mild, moderate, severe
    description = Column(Text)
    causes = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Recommendation(Base):
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"))
    category = Column(String)  # remedies, products, diet, precautions
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)  # face_wash, moisturizer, serum, sunscreen
    brand = Column(String)
    price_range = Column(String)
    image_url = Column(String)
    description = Column(Text)
    purchase_link = Column(String)
    recommended_for = Column(String)  # comma-separated disease names
    created_at = Column(DateTime, default=datetime.utcnow)
