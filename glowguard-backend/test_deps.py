"""
GlowGuard Backend - Minimal Test Server
This version tests dependencies one by one
"""

import sys

print("Testing GlowGuard Backend Dependencies...")
print("=" * 50)

packages_to_test = [
    ("fastapi", "FastAPI Framework"),
    ("uvicorn", "ASGI Server"),
    ("pydantic", "Data validation"),
    ("sqlalchemy", "Database ORM"),
]

installed = []
missing = []

for package_name, description in packages_to_test:
    try:
        __import__(package_name)
        print(f"✅ {package_name:20} - {description}")
        installed.append(package_name)
    except ImportError:
        print(f"❌ {package_name:20} - {description} (MISSING)")
        missing.append(package_name)

print("=" * 50)
print()

if missing:
    print(f"⚠️  {len(missing)} package(s) missing:")
    for pkg in missing:
        print(f"   - {pkg}")
    print()
    print("📦 To install missing packages, run:")
    print(f"   {sys.executable} -m pip install {' '.join(missing)}")
    print()
else:
    print("✅ All dependencies installed!")
    print()
    print("🚀 To start the backend server, run:")
    print("   python main.py")
    print()
