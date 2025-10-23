# 🚀 Quick Setup Guide - Full Stack

## Prerequisites
- Python 3.8+ (for backend)
- Node.js 18+ (for frontend)

---

## Backend Setup (Flask)

### 1. Navigate to backend folder
```powershell
cd backend
```

### 2. Create virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies
```powershell
pip install Flask Flask-CORS PyPDF2 pdfplumber python-dotenv Werkzeug Pillow pdfminer.six cryptography
```

### 4. Create .env file
```powershell
Copy-Item .env.example .env
```

### 5. Run backend
```powershell
python app.py
```

Backend will run on: **http://localhost:5000**

---

## Frontend Setup (React)

### 1. Open NEW terminal and navigate to frontend
```powershell
cd frontend
```

### 2. Install dependencies
```powershell
npm install
```

### 3. Run frontend
```powershell
npm run dev
```

Frontend will run on: **http://localhost:5173**

---

## 🎯 Access the Application

1. **Backend API**: http://localhost:5000
2. **Frontend UI**: http://localhost:5173

---

## ✅ Verify Everything Works

### Test Backend
```powershell
curl http://localhost:5000/health
```

### Test Frontend
Open browser: http://localhost:5173

---

## 📤 Test Upload

1. Go to http://localhost:5173
2. Drag and drop a credit card statement PDF
3. See the parsed results instantly!

---

## 🛑 Stop Servers

Press `Ctrl + C` in both terminal windows

---

## 📁 Project Structure

```
Sure_Finance/
├── backend/
│   ├── app.py              # Flask API
│   ├── config.py
│   ├── services/
│   │   └── pdf_parser.py
│   └── uploads/
│
└── frontend/
    ├── src/
    │   ├── App.jsx         # Main app
    │   ├── components/     # UI components
    │   └── index.css
    └── package.json
```

---

## 🐛 Common Issues

### Backend: Port 5000 in use
Edit `backend/.env`:
```
PORT=5001
```

Then update `frontend/src/App.jsx`:
```javascript
const API_BASE_URL = 'http://localhost:5001';
```

### Frontend: npm install fails
```powershell
rm -rf node_modules
rm package-lock.json
npm install
```

### CORS errors
Backend already has CORS enabled. If issues persist:
1. Check backend is running
2. Verify URLs match
3. Clear browser cache

---

## 🎉 You're All Set!

Upload a credit card statement PDF and watch the magic happen! ✨
