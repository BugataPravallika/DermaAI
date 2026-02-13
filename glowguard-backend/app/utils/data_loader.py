"""
Data loader utility for training datasets
Handles loading and preprocessing of HAM10000 and ISIC2018 datasets
"""

import os
from pathlib import Path

# Define base paths
BASE_DIR = Path(__file__).parent.parent.parent  # glowguard-backend/
DATA_DIR = BASE_DIR / "ml_models" / "training_data"

# Dataset paths
HAM10000_DIR = DATA_DIR / "HAM10000"
HAM10000_IMAGES_PART1 = HAM10000_DIR / "HAM10000_images_part_1"
HAM10000_IMAGES_PART2 = HAM10000_DIR / "HAM10000_images_part_2"
HAM10000_METADATA = HAM10000_DIR / "HAM10000_metadata.csv"

ISIC2018_DIR = DATA_DIR / "ISIC2018"
ISIC2018_TEST_IMAGES = ISIC2018_DIR / "ISIC2018_Task3_Test_Images"
ISIC2018_GROUND_TRUTH = ISIC2018_DIR / "ISIC2018_Task3_Test_GroundTruth.csv"


def verify_dataset_structure():
    """Verify that all required dataset files exist"""
    required_paths = [
        HAM10000_IMAGES_PART1,
        HAM10000_IMAGES_PART2,
        HAM10000_METADATA,
        ISIC2018_TEST_IMAGES,
        ISIC2018_GROUND_TRUTH,
    ]
    
    missing = []
    for path in required_paths:
        if not path.exists():
            missing.append(str(path))
    
    if missing:
        print("Warning: Missing dataset files:")
        for path in missing:
            print(f"  - {path}")
        return False
    
    print("✓ All dataset files found")
    return True


def get_ham10000_image_paths():
    """Get all HAM10000 image file paths"""
    image_paths = []
    
    for part_dir in [HAM10000_IMAGES_PART1, HAM10000_IMAGES_PART2]:
        if part_dir.exists():
            image_paths.extend(list(part_dir.glob("*.jpg")))
    
    return image_paths


def get_isic2018_image_paths():
    """Get all ISIC2018 test image file paths"""
    if ISIC2018_TEST_IMAGES.exists():
        return list(ISIC2018_TEST_IMAGES.glob("*.jpg"))
    return []


if __name__ == "__main__":
    # Test the data loader
    print("Dataset Structure Verification")
    print("=" * 50)
    print(f"Data Directory: {DATA_DIR}")
    print()
    
    verify_dataset_structure()
    
    print(f"\nHAM10000 Images: {len(get_ham10000_image_paths())} files")
    print(f"ISIC2018 Images: {len(get_isic2018_image_paths())} files")
