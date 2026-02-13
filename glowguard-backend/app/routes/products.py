"""Products routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Product
from app.utils.database import get_db
from typing import List

router = APIRouter()

@router.get("/")
async def get_all_products(db: Session = Depends(get_db)):
    """Get all products"""
    products = db.query(Product).all()
    return products

@router.get("/by-category/{category}")
async def get_products_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    """Get products by category"""
    products = db.query(Product).filter(Product.category == category).all()
    return products

@router.get("/recommended/{disease}")
async def get_recommended_products(
    disease: str,
    db: Session = Depends(get_db)
):
    """Get products recommended for a specific disease"""
    products = db.query(Product).filter(
        Product.recommended_for.contains(disease)
    ).all()
    return products

@router.get("/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get specific product"""
    product = db.query(Product).filter(Product.id == product_id).first()
    return product
