from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
from app.routes import auth, products, recommendations, users
from app.utils.database import init_db

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="GlowGuard - AI Skin Care Platform",
    description="AI-powered skin disease prediction and skincare guidance platform",
    version="1.0.0"
)

# Configure CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if not os.path.exists("uploads"):
    os.makedirs("uploads")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Initialize database
@app.on_event("startup")
async def startup():
    init_db()
    print("Database initialized")

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
# Attempt to load predictions router only if its optional dependencies are available
try:
    from app.routes import predictions
    app.include_router(predictions.router, prefix="/api/predictions", tags=["Predictions"])
except Exception as e:
    print("Predictions router not loaded (optional):", e)
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(recommendations.router, prefix="/api/recommendations", tags=["Recommendations"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to GlowGuard API",
        "version": "1.0.0",
        "status": "Running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("API_PORT", 8000)),
        reload=os.getenv("DEBUG", False)
    )
