"""
Seeds database with sample products for different skin conditions
Run this script once to populate the database with recommended products
"""

import sys
sys.path.insert(0, '/glowguard-backend')

from app.models import Product
from app.utils.database import SessionLocal

def seed_products():
    """Add sample products to database"""
    db = SessionLocal()
    
    products = [
        # Acne Products
        Product(
            name="Neutrogena Acne Wash",
            category="face_wash",
            brand="Neutrogena",
            price_range="$5-10",
            description="Gentle salicylic acid face wash for acne-prone skin",
            purchase_link="https://amazon.com/Neutrogena-Acne-Wash/dp/...",
            recommended_for="Acne",
        ),
        Product(
            name="CeraVe Facial Moisturizing Lotion",
            category="moisturizer",
            brand="CeraVe",
            price_range="$10-15",
            description="Lightweight, non-comedogenic moisturizer with ceramides",
            purchase_link="https://amazon.com/CeraVe-Moisturizing-Lotion/dp/...",
            recommended_for="Acne",
        ),
        Product(
            name="The Ordinary Niacinamide 10% + Zinc 1%",
            category="serum",
            brand="The Ordinary",
            price_range="$5-8",
            description="Reduces sebum, minimizes pores, controls acne",
            purchase_link="https://deciem.com/product/the-ordinary-niacinamide-10-zinc-1",
            recommended_for="Acne",
        ),
        Product(
            name="Neutrogena Ultra Sheer Dry-Touch Sunscreen",
            category="sunscreen",
            brand="Neutrogena",
            price_range="$8-12",
            description="SPF 50+ non-comedogenic sunscreen for acne-prone skin",
            purchase_link="https://amazon.com/Neutrogena-Ultra-Sheer-Dry-Touch-Sunscreen/dp/...",
            recommended_for="Acne",
        ),
        
        # Eczema Products
        Product(
            name="CeraVe Hydrating Cleanser",
            category="face_wash",
            brand="CeraVe",
            price_range="$10-12",
            description="Gentle, creamy cleanser for sensitive and eczema-prone skin",
            purchase_link="https://amazon.com/CeraVe-Hydrating-Cleanser/dp/...",
            recommended_for="Eczema",
        ),
        Product(
            name="Eucerin Eczema Relief Cream",
            category="moisturizer",
            brand="Eucerin",
            price_range="$12-18",
            description="Intensive cream with colloidal oatmeal for eczema relief",
            purchase_link="https://amazon.com/Eucerin-Eczema-Relief-Cream/dp/...",
            recommended_for="Eczema",
        ),
        Product(
            name="Aveeno Eczema Therapy Serum",
            category="serum",
            brand="Aveeno",
            price_range="$8-12",
            description="Oat extract serum to soothe itchy, eczema-prone skin",
            purchase_link="https://amazon.com/Aveeno-Eczema-Therapy-Serum/dp/...",
            recommended_for="Eczema",
        ),
        
        # Psoriasis Products
        Product(
            name="Head & Shoulders Therapeutic Shampoo",
            category="face_wash",
            brand="Head & Shoulders",
            price_range="$6-10",
            description="Zinc pyrithione shampoo effective for scalp psoriasis",
            purchase_link="https://amazon.com/Head-Shoulders-Therapeutic-Shampoo/dp/...",
            recommended_for="Psoriasis",
        ),
        Product(
            name="Cetaphil Rich Hydrating Night Cream",
            category="moisturizer",
            brand="Cetaphil",
            price_range="$15-20",
            description="Deep moisturizing cream for psoriasis and sensitive skin",
            purchase_link="https://amazon.com/Cetaphil-Rich-Hydrating-Night-Cream/dp/...",
            recommended_for="Psoriasis",
        ),
        
        # Dermatitis Products
        Product(
            name="La Roche-Posay Toleriane Hydrating Gentle Cleanser",
            category="face_wash",
            brand="La Roche-Posay",
            price_range="$10-14",
            description="Gentle, fragrance-free cleanser for dermatitis-prone skin",
            purchase_link="https://amazon.com/La-Roche-Posay-Toleriane-Hydrating-Cleanser/dp/...",
            recommended_for="Dermatitis",
        ),
        Product(
            name="Cetaphil Moisturizing Cream",
            category="moisturizer",
            brand="Cetaphil",
            price_range="$12-16",
            description="Fragrance-free, dermatologist-recommended moisturizer",
            purchase_link="https://amazon.com/Cetaphil-Moisturizing-Cream/dp/...",
            recommended_for="Dermatitis",
        ),
    ]
    
    # Add products to database
    for product in products:
        existing = db.query(Product).filter(Product.name == product.name).first()
        if not existing:
            db.add(product)
    
    db.commit()
    print(f"✅ Added {len(products)} products to database")
    db.close()

if __name__ == "__main__":
    seed_products()
