# Credit Card Statement Parser - Frontend

Modern, professional React frontend for the Credit Card Statement Parser application.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- Backend server running on `http://localhost:5000`

### Installation & Run

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`

## 🎨 Features

- ✅ **Drag & Drop Upload** - Intuitive file upload
- ✅ **Real-time Processing** - Instant parsing results  
- ✅ **Batch Upload** - Multiple files at once
- ✅ **Responsive Design** - Works on all devices
- ✅ **Beautiful UI** - Modern gradient design
- ✅ **Stats Dashboard** - Parsing statistics
- ✅ **Issuer Support** - All 5 major issuers
- ✅ **Export JSON** - Download parsed data

## 🛠️ Tech Stack

- React 19 + Vite
- Tailwind CSS 4
- Fetch API

## 📁 Components

```
src/components/
├── Header.jsx          # Navigation & branding
├── UploadZone.jsx      # Drag & drop upload
├── ResultsDisplay.jsx  # Results container
├── ResultCard.jsx      # Individual result
├── StatsCards.jsx      # Statistics
├── IssuerBadges.jsx    # Supported banks
└── Footer.jsx          # Footer info
```

## 🔌 API Integration

Backend URL: `http://localhost:5000`

Endpoints:
- `POST /api/parse` - Single file
- `POST /api/batch-parse` - Multiple files

## 🎨 Design Features

- Custom animations & transitions
- Gradient theming
- Smooth hover effects  
- Progress indicators
- Error handling UI
- Mobile-responsive

## 🚀 Build for Production

```bash
npm run build
npm run preview
```

---

**Built with ❤️ for Sure Finance Hackathon**
