.env.example: Template for environment variables - Copy and fill with your values
requirements.txt: List of Python dependencies
main.py: FastAPI application entry point

Directory Structure:
- app/models: Database models
- app/routes: API endpoint handlers
- app/schemas: Pydantic request/response schemas
- app/services: Business logic
- app/utils: Helper functions (auth, image processing, ML)
- ml_models: Pre-trained ML models storage
- uploads: User uploaded images storage

To get started:
1. Copy .env.example to .env
2. Run: pip install -r requirements.txt
3. Run: python main.py
