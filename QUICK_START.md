# Quick Start Guide

## For Impatient Developers 🚀

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend (5 minutes)

```bash
cd glowguard-backend

# Setup virtual env
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)

# Install & run
pip install -r requirements.txt
python main.py
```

✅ Server running at: http://localhost:8000

### Frontend (5 minutes)

```bash
cd glowguard-frontend

npm install
npm run dev
```

✅ Frontend running at: http://localhost:3000

### Test It!

1. Open http://localhost:3000
2. Click "Sign Up" → Create account
3. Click "Analyze" → Upload skin image
4. View results!

### API Docs

- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Project Overview

**GlowGuard** = AI Skin Disease Detector + Personalized Skincare Guide

**Tech Stack:**
- Backend: FastAPI (Python)
- Frontend: React (JavaScript)
- Database: SQLite (upgradeable to PostgreSQL)
- ML: TensorFlow with ResNet
- Styling: Tailwind CSS

**Features:**
- 📸 Upload skin photo
- 🤖 AI predicts disease
- 📊 Shows confidence %
- 🌿 Natural remedies
- 💄 Product recommendations
- 🥗 Diet advice
- ⚠️ Safety precautions

---

## File Structure

```
AI-skincare/
├── glowguard-backend/     ← Python/FastAPI
│   ├── main.py           ← Run this
│   ├── app/routes/       ← API endpoints
│   └── ml_models/        ← ML models
├── glowguard-frontend/    ← React/JavaScript
│   ├── src/App.jsx       ← Main component
│   └── src/pages/        ← Page components
└── docs/                 ← Documentation
```

---

## Common Commands

### Backend
```bash
cd glowguard-backend

# First time
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python main.py

# Test API
curl http://localhost:8000/health
```

### Frontend
```bash
cd glowguard-frontend

# First time
npm install

# Run
npm run dev

# Build
npm run build
```

---

## Environment Variables

### Backend (.env)
```
DATABASE_URL=sqlite:///./glowguard.db
SECRET_KEY=your-secret-key-change-this
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)
```
VITE_API_URL=http://localhost:8000/api
```

---

## Troubleshooting

**Port already in use?**
```bash
# macOS/Linux
lsof -i :8000
lsof -i :3000

# Windows
netstat -ano | findstr :8000
netstat -ano | findstr :3000
```

**Database error?**
```bash
cd glowguard-backend
rm glowguard.db
python main.py  # Creates new database
```

**Dependencies not installing?**
```bash
pip install -r requirements.txt --upgrade --no-cache-dir
```

---

## Next Steps

1. ✅ Run backend & frontend
2. 📱 Create account
3. 📸 Upload skin image
4. 🎯 Get AI prediction
5. 📚 Read docs for more features

---

## Important Links

- 📖 Full README: [README.md](../README.md)
- 📚 Setup Guide: [docs/SETUP_GUIDE.md](../docs/SETUP_GUIDE.md)
- 🔌 API Docs: [docs/API_DOCUMENTATION.md](../docs/API_DOCUMENTATION.md)
- 🗺️ Roadmap: [docs/ROADMAP.md](../docs/ROADMAP.md)

---

**Still stuck?** Check the docs or create an issue! 🆘
