"""Users routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import UserResponse, UserUpdate
from app.models import User
from app.utils.database import get_db
from app.utils.auth import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer() 
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
    """Get current authenticated user"""
    payload = verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    """Get current user profile"""
    return current_user

@router.put("/profile", response_model=UserResponse)
async def update_profile(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update user profile"""
    if user_update.full_name:
        current_user.full_name = user_update.full_name
    if user_update.age:
        current_user.age = user_update.age
    if user_update.skin_type:
        current_user.skin_type = user_update.skin_type
    
    db.commit()
    db.refresh(current_user)
    
    return current_user

@router.delete("/account")
async def delete_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete user account"""
    db.delete(current_user)
    db.commit()
    
    return {"message": "Account deleted successfully"}
@router.get("/admin/all-users")
async def get_all_users(db: Session = Depends(get_db)):
    """
    ✅ ADMIN ENDPOINT: View all registered users
    Use this to see who signed up!
    """
    users = db.query(User).all()
    
    return {
        "total_users": len(users),
        "users": [
            {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "full_name": user.full_name,
                "skin_type": user.skin_type,
                "created_at": user.created_at.isoformat() if user.created_at else None,
                "is_active": user.is_active,
            }
            for user in users
        ]
    }

@router.get("/admin/stats")
async def get_user_stats(db: Session = Depends(get_db)):
    """
    ✅ ADMIN ENDPOINT: Get user statistics
    """
    total_users = db.query(User).count()
    active_users = db.query(User).filter(User.is_active == True).count()
    inactive_users = db.query(User).filter(User.is_active == False).count()
    
    return {
        "total_registered_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users,
    }