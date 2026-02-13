"""LLM utilities for generating personalized advice"""
import os
from typing import List, Dict

class RecommendationEngine:
    """Generate recommendations using templates and rules"""
    
    NATURAL_REMEDIES = {
        "Acne": [
            "Tea tree oil: Apply diluted tea tree oil (2-3 drops in carrier oil) to affected areas",
            "Honey mask: Apply raw honey as a face mask for 15-20 minutes, 2-3 times weekly",
            "Aloe vera gel: Apply fresh aloe vera gel to calm inflammation",
            "Green tea: Use cooled green tea as a face wash or compress",
            "Lemon juice: Dilute with water and use as a spot treatment (use sunscreen after)"
        ],
        "Eczema": [
            "Coconut oil: Apply virgin coconut oil to moisturize dry areas",
            "Oatmeal bath: Soak in warm water with colloidal oatmeal for 15-20 minutes",
            "Aloe vera: Apply aloe vera gel to soothe irritated skin",
            "Apple cider vinegar: Dilute and apply as a rinse (patch test first)",
            "Chamomile: Use chamomile tea bags as warm compresses"
        ],
        "Psoriasis": [
            "Dead Sea salt bath: Soak for 10-15 minutes to reduce scaling",
            "Aloe vera: Apply aloe vera gel to reduce inflammation",
            "Turmeric: Mix with coconut oil for anti-inflammatory benefits",
            "Apple cider vinegar: Dilute and use as a rinse",
            "Moisturize heavily: Use natural oils like jojoba or argan oil"
        ],
        "Fungal Infection": [
            "Tea tree oil: Apply diluted tea tree oil to affected areas daily",
            "Apple cider vinegar: Soak affected areas in diluted apple cider vinegar",
            "Garlic: Apply crushed garlic mixed in coconut oil",
            "Neem oil: Apply neem oil for antifungal properties",
            "Keep dry: Ensure area is dry, use talc-free powder if needed"
        ],
        "Dermatitis": [
            "Coconut oil: Use as a natural moisturizer",
            "Oatmeal: Create a paste and apply to affected areas",
            "Aloe vera: Apply to soothe irritation",
            "Avoid irritants: Identify and avoid triggering substances",
            "Colloidal oatmeal bath: Soak to reduce itching"
        ]
    }
    
    DIET_ADVICE = {
        "Acne": {
            "eat": [
                "Fatty fish (salmon, mackerel) - rich in omega-3 fatty acids",
                "Berries - high in antioxidants",
                "Leafy greens (spinach, kale) - contain vitamins and minerals",
                "Green tea - has anti-inflammatory properties",
                "Dark chocolate (70%+ cocoa) - in moderation"
            ],
            "avoid": [
                "Dairy products - may trigger acne",
                "High-glycemic foods (white bread, sugary items)",
                "Processed foods with trans fats",
                "High-iodine foods (seaweed, shellfish)",
                "Excess sugar and refined carbohydrates"
            ],
            "water": "8-10 glasses daily",
            "supplements": ["Zinc", "Vitamin A", "Vitamin E", "B-complex vitamins"]
        },
        "Eczema": {
            "eat": [
                "Fatty fish - omega-3 reduces inflammation",
                "Olive oil - anti-inflammatory",
                "Fruits and vegetables - antioxidants",
                "Nuts and seeds - essential fatty acids",
                "Probiotics (yogurt, kefir) - supports immune health"
            ],
            "avoid": [
                "Common allergens (eggs, peanuts, tree nuts, dairy)",
                "Processed foods - may trigger flare-ups",
                "Alcohol - can irritate skin",
                "Spicy foods - may trigger reactions",
                "Foods with artificial additives"
            ],
            "water": "8-10 glasses daily",
            "supplements": ["Omega-3", "Vitamin D", "Probiotics", "Quercetin"]
        },
        "Psoriasis": {
            "eat": [
                "Fatty fish - omega-3s reduce inflammation",
                "Fruits and vegetables - antioxidants",
                "Whole grains - fiber and nutrients",
                "Olive oil - anti-inflammatory",
                "Turmeric - contains curcumin with healing properties"
            ],
            "avoid": [
                "Refined sugars - worsen inflammation",
                "Trans fats and excessive saturated fats",
                "Alcohol - triggers flare-ups",
                "Processed meats",
                "Nightshade vegetables (tomatoes, peppers) - may trigger in some"
            ],
            "water": "10-12 glasses daily",
            "supplements": ["Fish oil", "Vitamin D", "Vitamin B12", "Folic acid"]
        }
    }
    
    PRECAUTIONS = {
        "Acne": [
            "⚠️ Do not squeeze or pick at pimples - can lead to scarring and infection",
            "Use only dermatologist-approved products",
            "Wash face max 2 times daily - more can irritate skin",
            "Avoid touching your face throughout the day",
            "Change pillowcases frequently",
            "Remove makeup before sleeping",
            "Use oil-free makeup and sunscreen",
            "Avoid tight headwear",
            "Do not over-exfoliate - max 2-3 times per week"
        ],
        "Eczema": [
            "Avoid scratching - can lead to infection",
            "Use fragrance-free, hypoallergenic products only",
            "Take lukewarm baths/showers, not hot",
            "Pat skin dry gently, don't rub",
            "Moisturize within 3 minutes of bathing",
            "Wear soft, breathable fabrics (cotton, silk)",
            "Avoid harsh detergents and soaps",
            "Minimize stress through relaxation techniques",
            "Maintain consistent humidity in your environment"
        ],
        "Psoriasis": [
            "Avoid skin injuries and cuts - triggers lesions",
            "Manage stress effectively",
            "Sleep 7-9 hours daily",
            "Avoid smoking and limit alcohol",
            "Maintain moderate temperature - avoid extremes",
            "Keep skin moisturized to reduce scaling",
            "Avoid harsh soaps and detergents",
            "Protect from sun but get moderate sun exposure",
            "Follow prescribed treatments consistently"
        ]
    }
    
    WHEN_TO_SEE_DERMATOLOGIST = {
        "Acne": [
            "When over-the-counter treatments show no improvement after 6-8 weeks",
            "If acne is spreading rapidly",
            "For cystic acne (deep, painful bumps)",
            "If acne is affecting your mental health",
            "For severe inflammation or scarring"
        ],
        "Eczema": [
            "If self-care measures don't improve symptoms",
            "When affected areas show signs of infection (warmth, pus, fever)",
            "For severe itching affecting sleep or daily activities",
            "If the condition is worsening or spreading rapidly",
            "For personalized treatment plan and prescription options"
        ],
        "Psoriasis": [
            "If over-the-counter treatments are ineffective",
            "When patches cover significant body area",
            "For joint pain (psoriatic arthritis)",
            "If psoriasis is affecting mental health",
            "For guidance on systemic medications if needed"
        ]
    }
    
    @staticmethod
    def get_remedies(disease_name: str) -> List[str]:
        """Get natural remedies for a disease"""
        return RecommendationEngine.NATURAL_REMEDIES.get(disease_name, [])
    
    @staticmethod
    def get_diet_advice(disease_name: str) -> Dict:
        """Get diet advice for a disease"""
        return RecommendationEngine.DIET_ADVICE.get(
            disease_name,
            {
                "eat": ["Fruits and vegetables", "Plenty of water"],
                "avoid": ["Processed foods", "Sugar"],
                "water": "8-10 glasses daily",
                "supplements": []
            }
        )
    
    @staticmethod
    def get_precautions(disease_name: str) -> List[str]:
        """Get precautions for a disease"""
        return RecommendationEngine.PRECAUTIONS.get(disease_name, [])
    
    @staticmethod
    def get_dermatologist_guidance(disease_name: str) -> List[str]:
        """Get guidance on when to see a dermatologist"""
        return RecommendationEngine.WHEN_TO_SEE_DERMATOLOGIST.get(disease_name, [])
