"""
Model training script for skin disease classification
Trains on HAM10000 and ISIC2018 datasets
"""

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import json
import warnings
warnings.filterwarnings('ignore')

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.utils.data_loader import (
    HAM10000_IMAGES_PART1, HAM10000_IMAGES_PART2, HAM10000_METADATA,
    ISIC2018_TEST_IMAGES, ISIC2018_GROUND_TRUTH
)

# Configuration
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10
VALIDATION_SPLIT = 0.2
RANDOM_STATE = 42

# Disease labels mapping
DISEASE_LABELS = {
    'bkl': 'Keratosis',
    'nv': 'Nevus',
    'mel': 'Melanoma',
    'akiec': 'Actinic Keratosis',
    'bcc': 'Basal Cell Carcinoma',
    'vasc': 'Vascular Lesion',
    'df': 'Dermatofibroma'
}

class SkinDiseaseTrainer:
    """Trainer for skin disease classification models"""
    
    def __init__(self):
        self.model = None
        self.history = None
        self.label_encoder = LabelEncoder()
        self.class_labels = {}
        
    def load_ham10000_data(self):
        """Load HAM10000 dataset"""
        print("\n" + "="*60)
        print("Loading HAM10000 Dataset")
        print("="*60)
        
        # Load metadata
        metadata = pd.read_csv(HAM10000_METADATA)
        print(f"Total HAM10000 records: {len(metadata)}")
        print(f"\nDisease distribution:")
        print(metadata['dx'].value_counts())
        
        images = []
        labels = []
        image_ids = []
        
        # Load images from both parts
        for part_dir in [HAM10000_IMAGES_PART1, HAM10000_IMAGES_PART2]:
            if not part_dir.exists():
                print(f"Warning: {part_dir} not found")
                continue
                
            for image_id in metadata['image_id']:
                img_path = part_dir / f"{image_id}.jpg"
                
                if img_path.exists():
                    try:
                        # Load and resize image
                        img = load_img(str(img_path), target_size=(IMG_SIZE, IMG_SIZE))
                        img_array = img_to_array(img) / 255.0
                        
                        # Get label
                        label = metadata[metadata['image_id'] == image_id]['dx'].values[0]
                        
                        images.append(img_array)
                        labels.append(label)
                        image_ids.append(image_id)
                    except Exception as e:
                        print(f"Error loading {img_path}: {e}")
        
        print(f"\nSuccessfully loaded {len(images)} images")
        return np.array(images), np.array(labels), image_ids
    
    def load_isic2018_data(self):
        """Load ISIC2018 dataset"""
        print("\n" + "="*60)
        print("Loading ISIC2018 Dataset")
        print("="*60)
        
        if not ISIC2018_TEST_IMAGES.exists() or not ISIC2018_GROUND_TRUTH.exists():
            print("Warning: ISIC2018 dataset not found")
            return np.array([]), np.array([]), []
        
        # Load ground truth
        ground_truth = pd.read_csv(ISIC2018_GROUND_TRUTH)
        print(f"Total ISIC2018 records: {len(ground_truth)}")
        
        images = []
        labels = []
        image_ids = []
        
        # Load images
        for idx, row in ground_truth.iterrows():
            image_id = row.iloc[0]  # First column is image_id
            img_path = ISIC2018_TEST_IMAGES / f"{image_id}.jpg"
            
            if img_path.exists():
                try:
                    img = load_img(str(img_path), target_size=(IMG_SIZE, IMG_SIZE))
                    img_array = img_to_array(img) / 255.0
                    
                    # Get label from ground truth (find the column with value 1)
                    label = row.idxmax() if len(row) > 1 else 'unknown'
                    
                    images.append(img_array)
                    labels.append(label)
                    image_ids.append(image_id)
                except Exception as e:
                    print(f"Error loading {img_path}: {e}")
        
        print(f"Successfully loaded {len(images)} images")
        return np.array(images), np.array(labels), image_ids
    
    def prepare_data(self, X_ham, y_ham, X_isic=None, y_isic=None):
        """Prepare and encode labels"""
        print("\n" + "="*60)
        print("Preparing Data")
        print("="*60)
        
        # Combine datasets
        if X_isic is not None and len(X_isic) > 0:
            X = np.concatenate([X_ham, X_isic], axis=0)
            y = np.concatenate([y_ham, y_isic], axis=0)
            print(f"Combined dataset: {len(X)} images")
        else:
            X = X_ham
            y = y_ham
            print(f"Using HAM10000 dataset: {len(X)} images")
        
        # Encode labels
        self.label_encoder.fit(y)
        y_encoded = self.label_encoder.transform(y)
        self.class_labels = {i: label for i, label in enumerate(self.label_encoder.classes_)}
        
        print(f"Classes: {self.class_labels}")
        print(f"Label distribution:")
        unique, counts = np.unique(y_encoded, return_counts=True)
        for u, c in zip(unique, counts):
            print(f"  {self.class_labels[u]}: {c}")
        
        # Split data
        X_train, X_val, y_train, y_val = train_test_split(
            X, y_encoded, test_size=VALIDATION_SPLIT, random_state=RANDOM_STATE, stratify=y_encoded
        )
        
        print(f"\nTrain set: {len(X_train)} images")
        print(f"Validation set: {len(X_val)} images")
        
        return X_train, X_val, y_train, y_val
    
    def build_model(self, num_classes):
        """Build transfer learning model"""
        print("\n" + "="*60)
        print("Building Model")
        print("="*60)
        
        # Load pre-trained EfficientNetB3
        base_model = EfficientNetB3(
            input_shape=(IMG_SIZE, IMG_SIZE, 3),
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model layers
        base_model.trainable = False
        
        # Add custom layers
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(256, activation='relu')(x)
        x = Dropout(0.3)(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.2)(x)
        output = Dense(num_classes, activation='softmax')(x)
        
        self.model = Model(inputs=base_model.input, outputs=output)
        
        print(f"Model created with {num_classes} output classes")
        print(f"Total parameters: {self.model.count_params():,}")
        
        return self.model
    
    def train(self, X_train, X_val, y_train, y_val):
        """Train the model"""
        print("\n" + "="*60)
        print("Training Model")
        print("="*60)
        
        # Compile model
        self.model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        # Data augmentation
        train_datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            zoom_range=0.2,
            fill_mode='nearest'
        )
        
        # Callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True,
                verbose=1
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=3,
                min_lr=1e-6,
                verbose=1
            ),
            ModelCheckpoint(
                'ml_models/best_model.h5',
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1
            )
        ]
        
        # Train
        self.history = self.model.fit(
            train_datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
            validation_data=(X_val, y_val),
            epochs=EPOCHS,
            callbacks=callbacks,
            verbose=1
        )
        
        print("\nTraining completed!")
        
        return self.history
    
    def evaluate(self, X_val, y_val):
        """Evaluate model"""
        print("\n" + "="*60)
        print("Evaluating Model")
        print("="*60)
        
        loss, accuracy = self.model.evaluate(X_val, y_val, verbose=0)
        print(f"Validation Loss: {loss:.4f}")
        print(f"Validation Accuracy: {accuracy:.4f}")
        
        return loss, accuracy
    
    def save_model(self, model_path='ml_models/resnet_model.h5'):
        """Save trained model and class labels"""
        print("\n" + "="*60)
        print("Saving Model")
        print("="*60)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Save model
        self.model.save(model_path)
        print(f"Model saved to {model_path}")
        
        # Save class labels
        labels_path = os.path.join(os.path.dirname(model_path), 'class_labels.json')
        with open(labels_path, 'w') as f:
            json.dump(self.class_labels, f, indent=2)
        print(f"Class labels saved to {labels_path}")
    
    def plot_history(self, save_path='ml_models/training_history.png'):
        """Plot training history"""
        if self.history is None:
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Accuracy
        ax1.plot(self.history.history['accuracy'], label='Train Accuracy')
        ax1.plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Accuracy')
        ax1.set_title('Model Accuracy')
        ax1.legend()
        ax1.grid()
        
        # Loss
        ax2.plot(self.history.history['loss'], label='Train Loss')
        ax2.plot(self.history.history['val_loss'], label='Validation Loss')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Loss')
        ax2.set_title('Model Loss')
        ax2.legend()
        ax2.grid()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\nTraining history plot saved to {save_path}")
        plt.close()


def main():
    """Main training pipeline"""
    print("\n" + "="*60)
    print("SKIN DISEASE CLASSIFICATION MODEL TRAINING")
    print("="*60)
    
    trainer = SkinDiseaseTrainer()
    
    # Load data
    X_ham, y_ham, _ = trainer.load_ham10000_data()
    X_isic, y_isic, _ = trainer.load_isic2018_data()
    
    if len(X_ham) == 0:
        print("Error: No images loaded. Please check dataset paths.")
        return
    
    # Prepare data
    X_train, X_val, y_train, y_val = trainer.prepare_data(X_ham, y_ham, X_isic, y_isic)
    
    # Build model
    num_classes = len(np.unique(y_train))
    trainer.build_model(num_classes)
    
    # Train
    trainer.train(X_train, X_val, y_train, y_val)
    
    # Evaluate
    trainer.evaluate(X_val, y_val)
    
    # Save
    trainer.save_model()
    trainer.plot_history()
    
    print("\n" + "="*60)
    print("TRAINING COMPLETE!")
    print("="*60)
    print(f"Model saved to: ml_models/resnet_model.h5")
    print(f"Class labels saved to: ml_models/class_labels.json")


if __name__ == "__main__":
    main()
