#!/usr/bin/env python
"""
GlowGuard Backend - Dependency Installer
Run this script: python install.py
"""

import subprocess
import sys
import os

def install_requirements():
    """Install all required packages"""
    
    print("=" * 60)
    print("🚀 GlowGuard Backend - Dependency Installer")
    print("=" * 60)
    print()
    
    # Python version check
    print(f"🐍 Python {sys.version.split()[0]}")
    print()
    
    # Upgrade pip first
    print("📦 Upgrading pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    print("✅ pip upgraded\n")
    
    # Install minimal dependencies first
    minimal_packages = [
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "python-dotenv==1.0.0",
        "pydantic==2.5.0",
        "python-multipart==0.0.6",
        "sqlalchemy==2.0.23",
        "bcrypt==4.1.1",
        "pyjwt==2.8.1",
        "aiofiles==23.2.1",
        "requests==2.31.0",
    ]
    
    print("📚 Installing core packages...")
    for package in minimal_packages:
        print(f"  - Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"  ⚠️ Failed to install {package}, continuing...")
    
    print("\n✅ Core packages installed successfully!")
    print()
    
    # Optional packages (ML stuff - these can be installed later)
    print("⚠️  Note: Machine Learning packages (TensorFlow, PyTorch, OpenCV)")
    print("    are not installed in this minimal setup.")
    print("    Install them later when needed:")
    print()
    print("    pip install tensorflow==2.14.0")
    print("    pip install torchvision==0.16.1")
    print("    pip install opencv-python==4.8.1.78")
    print("    pip install pillow==10.1.0 numpy==1.24.3")
    print()
    
    print("=" * 60)
    print("✅ Installation Complete!")
    print("=" * 60)
    print()
    print("📍 To run the backend server:")
    print(f"   python main.py")
    print()
    print("📍 Or run directly:")
    print(f"   {sys.executable} main.py")
    print()

if __name__ == "__main__":
    try:
        install_requirements()
    except KeyboardInterrupt:
        print("\n\n⚠️ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)
