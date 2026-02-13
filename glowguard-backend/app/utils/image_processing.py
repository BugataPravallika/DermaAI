"""Image processing utilities"""
import cv2
import numpy as np
from PIL import Image
import os
from typing import Tuple

def process_image(image_path: str, target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Process image for ML model input
    
    Args:
        image_path: Path to the image file
        target_size: Target image size (height, width)
    
    Returns:
        Processed image array normalized for model input
    """
    try:
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read image file")
        
        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Resize
        img = cv2.resize(img, (target_size[1], target_size[0]))
        
        # Normalize to [0, 1]
        img = img.astype('float32') / 255.0
        
        return img
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")

def validate_image(file_path: str, max_size: int = 5242880) -> bool:
    """
    Validate image file
    
    Args:
        file_path: Path to image file
        max_size: Maximum file size in bytes
    
    Returns:
        True if valid, False otherwise
    """
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
    
    # Check file size
    if os.path.getsize(file_path) > max_size:
        return False
    
    # Check file extension
    ext = os.path.splitext(file_path)[1].lower().lstrip('.')
    if ext not in allowed_extensions:
        return False
    
    # Try to open with PIL
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except Exception:
        return False

def save_uploaded_file(uploaded_file, upload_dir: str = "uploads") -> str:
    """
    Save uploaded file to disk
    
    Args:
        uploaded_file: The uploaded file object
        upload_dir: Directory to save file
    
    Returns:
        Path to saved file
    """
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate unique filename
    import uuid
    from datetime import datetime
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    
    # Get file extension
    ext = os.path.splitext(uploaded_file.filename)[1]
    filename = f"{timestamp}_{unique_id}{ext}"
    
    file_path = os.path.join(upload_dir, filename)
    
    # Save file
    with open(file_path, "wb") as f:
        content = uploaded_file.file.read()
        f.write(content)
    
    return file_path
