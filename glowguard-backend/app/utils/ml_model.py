"""ML Model utilities"""
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from typing import Tuple, Dict
import json

class SkinDiseasePredictor:
    """Wrapper for skin disease prediction model"""
    
    def __init__(self, model_path: str = "ml_models/resnet_model.h5"):
        """Initialize the predictor with a pre-trained model"""
        self.model_path = model_path
        self.model = None
        self.class_labels = self._load_class_labels()
        self.load_model()
    
    def load_model(self):
        """Load the TensorFlow model"""
        try:
            if os.path.exists(self.model_path):
                self.model = tf.keras.models.load_model(self.model_path)
                print(f"Model loaded from {self.model_path}")
            else:
                print(f"Model not found at {self.model_path}. Using MobileNetV2 as fallback.")
                self._load_pretrained_model()
        except Exception as e:
            print(f"Error loading model: {e}")
            self._load_pretrained_model()
    
    def _load_pretrained_model(self):
        """Load a pre-trained MobileNetV2 model as fallback"""
        self.model = tf.keras.applications.MobileNetV2(
            input_shape=(224, 224, 3),
            include_top=True,
            weights='imagenet'
        )
    
    def _load_class_labels(self) -> Dict[int, str]:
        """Load disease class labels"""
        labels_path = "ml_models/class_labels.json"
        
        # Default labels for common skin diseases
        default_labels = {
            0: "Acne",
            1: "Eczema",
            2: "Psoriasis",
            3: "Fungal Infection",
            4: "Dermatitis",
            5: "Pigmentation Disorder",
            6: "Hemangioma",
            7: "Melanoma",
            8: "Nevus",
            9: "Healthy Skin"
        }
        
        if os.path.exists(labels_path):
            try:
                with open(labels_path, 'r') as f:
                    return json.load(f)
            except:
                return default_labels
        
        return default_labels
    
    def predict(self, image_array: np.ndarray) -> Tuple[str, float, int]:
        """
        Predict skin disease from image array
        
        Args:
            image_array: Preprocessed image array
        
        Returns:
            Tuple of (disease_name, confidence, class_index)
        """
        try:
            if self.model is None:
                raise Exception("Model not loaded")
            
            # Add batch dimension
            img_array = np.expand_dims(image_array, axis=0)
            
            # Predict
            predictions = self.model.predict(img_array, verbose=0)
            
            # Get top prediction
            class_idx = np.argmax(predictions[0])
            confidence = float(predictions[0][class_idx])
            disease_name = self.class_labels.get(class_idx, "Unknown Disease")
            
            return disease_name, confidence, class_idx
        
        except Exception as e:
            raise Exception(f"Error during prediction: {str(e)}")

class DiseaseDatabaseHandler:
    """Handle disease information database"""
    
    DISEASE_DATABASE = {
        "Acne": {
            "description": "Acne is a skin condition characterized by pimples, blackheads, and whiteheads. It typically appears on the face, chest, and back.",
            "causes": [
                "Excess oil production",
                "Clogged pores",
                "Bacterial growth",
                "Hormonal changes",
                "Certain medications"
            ],
            "severity_indicators": {
                "mild": "Occasional pimples and blackheads",
                "moderate": "Numerous pimples, pustules, and some redness",
                "severe": "Deep cystic acne, significant inflammation, widespread affected areas"
            }
        },
        "Eczema": {
            "description": "Eczema is an inflammatory skin condition causing itching, redness, and dry patches. It's often called atopic dermatitis.",
            "causes": [
                "Genetic predisposition",
                "Immune system dysfunction",
                "Environmental triggers",
                "Dry skin",
                "Stress"
            ],
            "severity_indicators": {
                "mild": "Slight itching and redness",
                "moderate": "Significant itching, visible redness, dry patches",
                "severe": "Intense itching, severe inflammation, blistering, skin thickening"
            }
        },
        "Psoriasis": {
            "description": "Psoriasis is an autoimmune skin condition causing thick, red, scaly patches. It's usually itchy or painful.",
            "causes": [
                "Genetic factors",
                "Immune system malfunction",
                "Stress",
                "Infections",
                "Medications"
            ],
            "severity_indicators": {
                "mild": "Small patches covering less than 3% of body",
                "moderate": "Patches covering 3-10% of body surface",
                "severe": "Patches covering more than 10% of body, significant pain/itching"
            }
        },
        "Fungal Infection": {
            "description": "Fungal infections of the skin are caused by fungal organisms. Common types include ringworm and athlete's foot.",
            "causes": [
                "Fungal organism exposure",
                "Warm, moist environment",
                "Poor hygiene",
                "Weakened immune system",
                "Skin injuries"
            ],
            "severity_indicators": {
                "mild": "Small localized patches with minimal symptoms",
                "moderate": "Larger affected areas with itching and redness",
                "severe": "Widespread infection, severe itching, secondary infections"
            }
        },
        "Dermatitis": {
            "description": "Dermatitis is inflammation of the skin caused by allergic reactions or irritants. Includes contact dermatitis and seborrheic dermatitis.",
            "causes": [
                "Allergic reactions",
                "Irritating substances",
                "Environmental factors",
                "Sensitivity to products",
                "Underlying conditions"
            ],
            "severity_indicators": {
                "mild": "Slight redness and itching",
                "moderate": "Visible inflammation, itching, possible blistering",
                "severe": "Severe inflammation, intense itching, widespread blistering, skin breakdown"
            }
        },
        "Pigmentation Disorder": {
            "description": "Pigmentation disorders result in abnormal coloring of the skin. Can appear as patches of lighter or darker skin.",
            "causes": [
                "Sun exposure",
                "Genetic factors",
                "Hormonal changes",
                "Skin injuries",
                "Inflammatory conditions"
            ],
            "severity_indicators": {
                "mild": "Minimal visible discoloration",
                "moderate": "Noticeable patches of discoloration",
                "severe": "Extensive discoloration, significant cosmetic impact"
            }
        }
    }
    
    @staticmethod
    def get_disease_info(disease_name: str) -> dict:
        """Get detailed information about a disease"""
        return DiseaseDatabaseHandler.DISEASE_DATABASE.get(
            disease_name,
            {
                "description": "Disease information not available",
                "causes": [],
                "severity_indicators": {}
            }
        )
    
    @staticmethod
    def get_severity_level(disease_name: str, confidence: float) -> str:
        """Estimate severity level based on confidence"""
        if confidence < 0.5:
            return "Not detected"
        elif confidence < 0.7:
            return "mild"
        elif confidence < 0.85:
            return "moderate"
        else:
            return "severe"
