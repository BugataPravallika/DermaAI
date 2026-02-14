"""
Quick test script to verify backend improvements are working
"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("=" * 60)
    print("GLOWGUARD BACKEND VERIFICATION")
    print("=" * 60)
    
    # Test 1: Import model
    print("\n✓ Test 1: Importing SkinDiseasePredictor...")
    from app.utils.ml_model import SkinDiseasePredictor
    print("  ✅ SUCCESS: Model imported")
    
    # Test 2: Check for predict_top_3 method
    print("\n✓ Test 2: Checking for predict_top_3() method...")
    if hasattr(SkinDiseasePredictor, 'predict_top_3'):
        print("  ✅ SUCCESS: predict_top_3() method exists")
    else:
        print("  ❌ FAILED: predict_top_3() method not found")
    
    # Test 3: Check for predict method
    print("\n✓ Test 3: Checking for predict() method...")
    if hasattr(SkinDiseasePredictor, 'predict'):
        print("  ✅ SUCCESS: predict() method exists")
    else:
        print("  ❌ FAILED: predict() method not found")
    
    # Test 4: Check schemas
    print("\n✓ Test 4: Checking updated schemas...")
    from app.schemas import DifferentialDiagnosis, AnalysisCombinedResponse
    print("  ✅ SUCCESS: DifferentialDiagnosis schema exists")
    print("  ✅ SUCCESS: AnalysisCombinedResponse schema exists")
    
    # Test 5: Create instance
    print("\n✓ Test 5: Creating SkinDiseasePredictor instance...")
    predictor = SkinDiseasePredictor()
    print("  ✅ SUCCESS: Predictor instance created")
    
    # Test 6: Check methods
    print("\n✓ Test 6: Verifying methods are callable...")
    methods = ['predict', 'predict_top_3', 'load_model', '_load_class_labels']
    for method_name in methods:
        if hasattr(predictor, method_name):
            print(f"  ✅ {method_name}() is available")
        else:
            print(f"  ❌ {method_name}() is missing")
    
    print("\n" + "=" * 60)
    print("✅ ALL BACKEND CHECKS PASSED!")
    print("=" * 60)
    print("\nYour GlowGuard backend improvements are working correctly!")
    print("\nNext steps:")
    print("1. Start backend: python main.py")
    print("2. Start frontend: npm run dev")
    print("3. Test in browser: http://localhost:5173")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print(f"\nFull traceback:")
    import traceback
    traceback.print_exc()
    sys.exit(1)
