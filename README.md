# GlowGuard - AI Skin Care Disease Prediction & Guidance Platform

Welcome to **GlowGuard**, a revolutionary AI-powered platform that helps users understand their skin conditions and receive personalized skincare guidance.

## 🎯 Project Overview

GlowGuard leverages cutting-edge artificial intelligence, computer vision, and deep learning to:

- **Analyze and predict** skin diseases from uploaded photos
- **Provide confidence scores** for each prediction
- **Deliver personalized recommendations** for remedies, products, diet, and precautions
- **Track progress** with before/after galleries
- **Offer professional guidance** with when to see a dermatologist

## ✨ Key Features

### 1. **AI-Powered Analysis**
- Uses CNN (ResNet/MobileNet) for accurate image classification
- Analyzes skin condition in seconds
- Returns prediction with confidence percentage

### 2. **Comprehensive Recommendations**
- 🌿 **Natural Remedies**: Safe home-based treatments
- 🧴 **Product Recommendations**: Dermatologist-approved skincare products
- 🥗 **Diet & Health Advice**: Foods to eat/avoid, vitamins, water intake
- ⚠️ **Safety & Precautions**: When to see a dermatologist

### 3. **Beautiful UI/UX**
- Soft pastel theme (pink, lavender, peach, beige)
- Smooth animations and transitions
- Mobile-responsive design
- Feminine, elegant aesthetic

### 4. **User Management**
- Secure authentication with JWT
- User profiles with skin type information
- Prediction history tracking
- Profile updates

### 5. **Data Persistence**
- Database storage for predictions
- User history management
- Recommendation storage

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite (default), PostgreSQL (production)
- **ML**: TensorFlow, PyTorch
- **Authentication**: JWT with bcrypt
- **API Documentation**: OpenAPI/Swagger

### Frontend
- **Framework**: React 18
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Animations**: Framer Motion
- **Icons**: React Icons
- **Build Tool**: Vite

### ML/AI
- **Model**: Pre-trained ResNet/MobileNet
- **Dataset**: HAM10000 (Skin Cancer dataset)
- **Image Processing**: OpenCV, PIL
- **Libraries**: TensorFlow/PyTorch

## 📁 Project Structure

```
AI-skincare/
├── glowguard-backend/          # FastAPI Backend
│   ├── app/
│   │   ├── models/             # SQLAlchemy models
│   │   ├── routes/             # API endpoints
│   │   ├── schemas/            # Pydantic schemas
│   │   ├── services/           # Business logic
│   │   └── utils/              # Utilities
│   ├── ml_models/              # Pre-trained ML models
│   ├── uploads/                # User uploaded images
│   ├── main.py                 # Entry point
│   └── requirements.txt         # Python dependencies
│
├── glowguard-frontend/         # React Frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── styles/             # CSS styles
│   │   ├── utils/              # Utils (API, store)
│   │   └── App.jsx             # Root component
│   ├── package.json            # Node dependencies
│   └── vite.config.js          # Vite configuration
│
└── docs/                       # Documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Pip and npm

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd glowguard-backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file:**
   ```bash
   cp .env.example .env
   ```
   
   Update `.env` with your configuration

5. **Run the server:**
   ```bash
   python main.py
   ```

   Server runs at: `http://localhost:8000`
   API Docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd glowguard-frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

   Frontend runs at: `http://localhost:3000`

## 📚 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user

### Predictions
- `POST /api/predictions/analyze` - Analyze skin image
- `GET /api/predictions/history/{user_id}` - Get prediction history
- `GET /api/predictions/{prediction_id}` - Get specific prediction

### Users
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update user profile
- `DELETE /api/users/account` - Delete account

### Products
- `GET /api/products/` - Get all products
- `GET /api/products/by-category/{category}` - Get products by category
- `GET /api/products/recommended/{disease}` - Get recommended products

### Recommendations
- `GET /api/recommendations/by-prediction/{prediction_id}` - Get recommendations

## 🔧 Configuration

### Environment Variables

Create `.env` file at `/glowguard-backend/`:

```
DATABASE_URL=sqlite:///./glowguard.db
SECRET_KEY=your-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
API_PORT=8000
DEBUG=True
CORS_ORIGINS=http://localhost:3000
MODEL_CONFIDENCE_THRESHOLD=0.6
```

## 🧠 Machine Learning

### Model Details
- **Type**: Convolutional Neural Network (CNN)
- **Base Architecture**: ResNet50 or MobileNetV2
- **Input Size**: 224x224 pixels
- **Output**: Disease classification with confidence scores

### Supported Conditions
1. Acne
2. Eczema
3. Psoriasis
4. Fungal Infection
5. Dermatitis
6. Pigmentation Disorders
7. Hemangioma
8. Melanoma
9. Nevus
10. Healthy Skin

### Model Usage
```python
from app.utils.ml_model import SkinDiseasePredictor
from app.utils.image_processing import process_image

predictor = SkinDiseasePredictor()
processed_img = process_image('image.jpg')
disease, confidence, class_idx = predictor.predict(processed_img)
```

## 🎨 Design System

### Color Palette
- **Primary Pink**: #FFD6E8
- **Lavender**: #E6D5F5
- **Peach**: #FFDAB9
- **Beige**: #F5E6D3
- **Cream**: #FFF8F3

### Typography
- **Headers**: Playfair Display (serif)
- **Body**: Poppins (sans-serif)

### Components
- Soft rounded corners (border-radius: 2rem)
- Subtle shadows and gradients
- Smooth transitions (0.3s)
- Pastel color overlays

## 🔐 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- Input validation with Pydantic
- Secure file upload handling
- SQL injection prevention (ORM)

## 📊 Database Schema

### Users Table
- id, email, username, hashed_password, full_name, age, skin_type, created_at, updated_at, is_active

### Predictions Table
- id, user_id, image_path, disease_name, confidence, severity, description, causes, timestamp

### Recommendations Table
- id, prediction_id, category, content, created_at

### Products Table
- id, name, category, brand, price_range, image_url, description, purchase_link, recommended_for

## 🧪 Testing

Run tests (when implemented):
```bash
pytest app/tests/
```

## 📱 Responsive Design

- Mobile-first approach
- Breakpoints: 640px (sm), 768px (md), 1024px (lg)
- Touch-friendly UI elements
- Optimized for all devices

## 🚢 Deployment

### Backend (Heroku/AWS/GCP)
```bash
# Build Docker image
docker build -t glowguard-backend .
docker run -p 8000:8000 glowguard-backend
```

### Frontend (Vercel/Netlify)
```bash
npm run build
# Deploy dist/ folder
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## ⚖️ License

This project is licensed under the MIT License.

## ⚠️ Important Disclaimer

**GlowGuard is NOT a medical diagnosis tool.** The predictions and recommendations provided are for informational and educational purposes only. 

**Always consult with a qualified dermatologist or healthcare professional for:**
- Medical diagnosis
- Treatment plans
- Prescription medications
- Severe skin conditions

The AI model's predictions should be used as a reference point only, not as a definitive diagnosis.

## 📞 Support

For issues, questions, or feedback:
- Email: support@glowguard.com
- GitHub Issues: [Create an issue]
- Twitter: @GlowGuardAI

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [TensorFlow Docs](https://www.tensorflow.org/docs)
- [Tailwind CSS](https://tailwindcss.com/)

---

**Made with ❤️ for beautiful, healthy skin**
