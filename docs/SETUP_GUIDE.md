# Setup & Installation Guide

## Step 1: Backend Setup

### 1.1 Install Python Dependencies

```bash
cd glowguard-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 1.2 Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
```

### 1.3 Initialize Database

The database will be initialized automatically when you first run the server.

### 1.4 Run Backend Server

```bash
python main.py
```

Server starts at `http://localhost:8000`

**API Documentation available at:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Step 2: Frontend Setup

### 2.1 Install Node Dependencies

```bash
cd glowguard-frontend

npm install
```

### 2.2 Run Development Server

```bash
npm run dev
```

Frontend starts at `http://localhost:3000`

### 2.3 Build for Production

```bash
npm run build
```

---

## Step 3: ML Model Setup (Optional)

### Downloading Pre-trained Models

1. Download MobileNetV2 or ResNet50 weights from TensorFlow Hub
2. Place in `glowguard-backend/ml_models/` directory
3. Update model path in `app.utils.ml_model.py`

```python
model = SkinDiseasePredictor(model_path="ml_models/your_model.h5")
```

---

## Common Issues & Solutions

### Issue: Port Already in Use

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### Issue: CORS Error

**Solution:** Check `CORS_ORIGINS` in `.env`:
```
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Issue: Database Error

**Solution:**
```bash
# Remove existing database
rm glowguard.db

# Restart server (will create new database)
python main.py
```

### Issue: Module Not Found

**Solution:**
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

---

## Testing the Application

### Test User Registration

```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "password123",
    "full_name": "Test User"
  }'
```

### Test Login

```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Test Image Upload (with token)

```bash
curl -X POST "http://localhost:8000/api/predictions/analyze" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -F "file=@/path/to/image.jpg"
```

---

## Database Management

### Reset Database

```bash
# Delete database file
rm glowguard.db

# Restart server to recreate
python main.py
```

### Backup Database

```bash
# Create backup
cp glowguard.db glowguard_backup.db
```

---

## Troubleshooting

### Backend Won't Start

1. Check Python version:
   ```bash
   python --version  # Should be 3.8+
   ```

2. Check virtual environment activation:
   ```bash
   which python  # Should show venv path
   ```

3. Install missing dependencies:
   ```bash
   pip install -r requirements.txt --no-cache-dir
   ```

### Frontend Build Issues

1. Clear npm cache:
   ```bash
   npm cache clean --force
   ```

2. Reinstall node_modules:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. Update npm:
   ```bash
   npm install -g npm@latest
   ```

---

## Next Steps

1. ✅ Backend and frontend are running
2. 📱 Visit `http://localhost:3000` in your browser
3. 🔐 Create an account
4. 📸 Upload a skin image for analysis
5. 📊 View results and recommendations

---

## Production Deployment

See `DEPLOYMENT.md` for production setup instructions.
