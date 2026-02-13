# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Authentication
All protected endpoints require JWT token in Authorization header:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## 📝 Authentication Endpoints

### 1. Register User
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password123",
  "full_name": "User Name",
  "age": 25,
  "skin_type": "oily"
}
```

**Response (200):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "User Name",
  "age": 25,
  "skin_type": "oily",
  "created_at": "2024-02-12T10:00:00",
  "is_active": true
}
```

### 2. Login User
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "full_name": "User Name",
    "age": 25,
    "skin_type": "oily",
    "created_at": "2024-02-12T10:00:00",
    "is_active": true
  }
}
```

### 3. Logout
```http
POST /auth/logout
Authorization: Bearer YOUR_TOKEN
```

**Response (200):**
```json
{
  "message": "Logged out successfully"
}
```

---

## 📸 Prediction Endpoints

### 1. Analyze Skin Image
```http
POST /predictions/analyze
Authorization: Bearer YOUR_TOKEN
Content-Type: multipart/form-data

file: [image file]
```

**Response (200):**
```json
{
  "prediction": {
    "id": 1,
    "user_id": 1,
    "image_path": "uploads/20240212_101234_abc12345.jpg",
    "disease_name": "Acne",
    "confidence": 0.92,
    "severity": "moderate",
    "description": "Acne is a skin condition...",
    "causes": "Excess oil production, Clogged pores, ...",
    "timestamp": "2024-02-12T10:00:00"
  },
  "analysis": {
    "disease_name": "Acne",
    "confidence": 0.92,
    "severity": "moderate",
    "description": "...",
    "causes": ["Excess oil", "Clogged pores"],
    "remedies": ["Tea tree oil...", "Honey mask..."],
    "precautions": ["Do not squeeze...", "Use dermatologist-approved..."],
    "diet_advice": {
      "eat": ["Fatty fish", "Berries"],
      "avoid": ["Dairy products", "Sugar"],
      "water": "8-10 glasses daily",
      "supplements": ["Zinc", "Vitamin A"]
    },
    "products": [
      {
        "id": 1,
        "name": "Neutrogena Acne Wash",
        "category": "face_wash",
        "brand": "Neutrogena",
        "price_range": "$5-10",
        "image_url": "...",
        "description": "...",
        "purchase_link": "https://amazon.com/...",
        "recommended_for": "Acne"
      }
    ]
  },
  "recommendations": [...]
}
```

### 2. Get Prediction History
```http
GET /predictions/history/{user_id}
Authorization: Bearer YOUR_TOKEN
```

**Response (200):**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "disease_name": "Acne",
    "confidence": 0.92,
    "severity": "moderate",
    "timestamp": "2024-02-12T10:00:00"
  },
  {
    "id": 2,
    "user_id": 1,
    "disease_name": "Eczema",
    "confidence": 0.85,
    "severity": "mild",
    "timestamp": "2024-02-10T15:30:00"
  }
]
```

### 3. Get Specific Prediction
```http
GET /predictions/{prediction_id}
Authorization: Bearer YOUR_TOKEN
```

**Response (200):** Same as Analyze endpoint

---

## 👤 User Endpoints

### 1. Get Profile
```http
GET /users/profile
Authorization: Bearer YOUR_TOKEN
```

**Response (200):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "User Name",
  "age": 25,
  "skin_type": "oily",
  "created_at": "2024-02-12T10:00:00",
  "is_active": true
}
```

### 2. Update Profile
```http
PUT /users/profile
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "full_name": "New Name",
  "age": 26,
  "skin_type": "combination"
}
```

**Response (200):** Updated user object

### 3. Delete Account
```http
DELETE /users/account
Authorization: Bearer YOUR_TOKEN
```

**Response (200):**
```json
{
  "message": "Account deleted successfully"
}
```

---

## 🛍️ Products Endpoints

### 1. Get All Products
```http
GET /products/
```

### 2. Get Products by Category
```http
GET /products/by-category/{category}
```

Categories: `face_wash`, `moisturizer`, `serum`, `sunscreen`

### 3. Get Recommended Products
```http
GET /products/recommended/{disease}
```

Example: `/products/recommended/Acne`

### 4. Get Specific Product
```http
GET /products/{product_id}
```

---

## 💊 Recommendations Endpoints

### 1. Get Recommendations by Prediction
```http
GET /recommendations/by-prediction/{prediction_id}
```

**Response (200):**
```json
{
  "remedies": [
    "Tea tree oil: Apply diluted...",
    "Honey mask: Apply raw honey..."
  ],
  "precautions": [
    "Do not squeeze or pick at pimples",
    "Use only dermatologist-approved products"
  ]
}
```

### 2. Get Recommendations by Category
```http
GET /recommendations/by-category/{category}
```

Categories: `remedies`, `products`, `diet`, `precautions`

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid image file"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid token"
}
```

### 403 Forbidden
```json
{
  "detail": "Access denied"
}
```

### 404 Not Found
```json
{
  "detail": "Prediction not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Error analyzing image: ..."
}
```

---

## Rate Limiting
- 100 requests per minute per user
- 1000 requests per day per user

---

## Data Types

### Severity Levels
- `mild`: Slight symptoms, minimal impact
- `moderate`: Noticeable symptoms, some impact
- `severe`: Significant impact on daily life

### Skin Types
- `oily`: Excess sebum production
- `dry`: Inadequate moisture
- `combination`: Mixed characteristics
- `normal`: Balanced condition

### Product Categories
- `face_wash`: Cleansing products
- `moisturizer`: Hydrating products
- `serum`: Concentrated treatments
- `sunscreen`: UV protection

---

## Advanced Usage Examples

### Upload and Analyze with cURL
```bash
curl -X POST \
  http://localhost:8000/api/predictions/analyze \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@path/to/image.jpg"
```

### Python Example
```python
import requests

headers = {"Authorization": "Bearer YOUR_TOKEN"}
files = {"file": open("image.jpg", "rb")}

response = requests.post(
  "http://localhost:8000/api/predictions/analyze",
  headers=headers,
  files=files
)

print(response.json())
```

### JavaScript Example
```javascript
const token = "YOUR_TOKEN";
const formData = new FormData();
formData.append("file", imageFile);

fetch("http://localhost:8000/api/predictions/analyze", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`
  },
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## API Response Headers

All responses include:
```
Content-Type: application/json
X-Process-Time: 0.123 (seconds)
```

---

**For interactive API documentation, visit:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
