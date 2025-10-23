# Credit Card Statement Parser - Flask Backend

A robust Flask backend API for parsing credit card statements (PDF) and extracting key data points from 5 major credit card issuers.

## 🎯 Features

- **Multi-Issuer Support**: Parses statements from 5 major issuers:
  - Chase
  - American Express
  - Citibank
  - Capital One
  - Discover

- **Data Extraction**: Extracts 10+ key data points:
  - Card Issuer
  - Card Last 4 Digits
  - Billing Cycle
  - Payment Due Date
  - Total Balance
  - Minimum Payment
  - Statement Date
  - Account Holder Name
  - Credit Limit
  - Available Credit

- **Advanced PDF Processing**: Uses multiple parsing libraries (pdfplumber & PyPDF2) for maximum compatibility
- **RESTful API**: Clean, well-documented API endpoints
- **Batch Processing**: Support for parsing multiple statements at once
- **Error Handling**: Comprehensive error handling and logging
- **CORS Enabled**: Ready for frontend integration

## 📋 Requirements

- Python 3.8+
- pip

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "d:\Web development\Hackathon\Sure_Finance"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   ```bash
   copy .env.example .env
   ```
   Edit `.env` file with your configuration (optional - defaults work fine for development)

## 🏃‍♂️ Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **The API will be available at**: `http://localhost:5000`

You should see:
```
============================================================
Credit Card Statement Parser API
============================================================
Server running on: http://localhost:5000
Supported Issuers: Chase, American Express, Citibank, Capital One, Discover
============================================================
```

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Health Check
```http
GET /
GET /health
```

**Response**:
```json
{
  "status": "success",
  "message": "Credit Card Statement Parser API",
  "version": "1.0.0"
}
```

---

#### 2. Get Supported Issuers
```http
GET /api/issuers
```

**Response**:
```json
{
  "status": "success",
  "supported_issuers": [
    "Chase",
    "American Express",
    "Citibank",
    "Capital One",
    "Discover"
  ],
  "count": 5
}
```

---

#### 3. Parse Statement (Single)
```http
POST /api/parse
```

**Request**:
- Content-Type: `multipart/form-data`
- Body:
  - `file`: PDF file (required)
  - `issuer`: Card issuer hint (optional)

**Example using cURL**:
```bash
curl -X POST http://localhost:5000/api/parse \
  -F "file=@statement.pdf" \
  -F "issuer=Chase"
```

**Example using Python**:
```python
import requests

url = "http://localhost:5000/api/parse"
files = {'file': open('statement.pdf', 'rb')}
data = {'issuer': 'Chase'}  # Optional

response = requests.post(url, files=files, data=data)
print(response.json())
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "card_issuer": "Chase",
    "card_last_4_digits": "1234",
    "billing_cycle": "2024-09-01 to 2024-09-30",
    "payment_due_date": "2024-10-25",
    "total_balance": "$1,234.56",
    "minimum_payment": "$35.00",
    "statement_date": "2024-09-30",
    "account_holder": "John Doe",
    "credit_limit": "$10,000.00",
    "available_credit": "$8,765.44",
    "extraction_confidence": "high"
  },
  "filename": "statement.pdf",
  "parsed_at": "2024-10-23T12:00:00"
}
```

---

#### 4. Batch Parse Statements
```http
POST /api/batch-parse
```

**Request**:
- Content-Type: `multipart/form-data`
- Body:
  - `files`: Multiple PDF files

**Example using cURL**:
```bash
curl -X POST http://localhost:5000/api/batch-parse \
  -F "files=@statement1.pdf" \
  -F "files=@statement2.pdf" \
  -F "files=@statement3.pdf"
```

**Response**:
```json
{
  "status": "success",
  "parsed_count": 3,
  "error_count": 0,
  "results": [
    {
      "filename": "statement1.pdf",
      "status": "success",
      "data": { /* extracted data */ }
    },
    // ... more results
  ],
  "errors": null,
  "parsed_at": "2024-10-23T12:00:00"
}
```

## 🧪 Testing the API

### Using the Test Script

Create a test file `test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000"

# Test health check
response = requests.get(f"{BASE_URL}/health")
print("Health Check:", response.json())

# Test supported issuers
response = requests.get(f"{BASE_URL}/api/issuers")
print("Supported Issuers:", response.json())

# Test parse statement (replace with your PDF file)
# with open('sample_statement.pdf', 'rb') as f:
#     files = {'file': f}
#     response = requests.post(f"{BASE_URL}/api/parse", files=files)
#     print("Parse Result:", json.dumps(response.json(), indent=2))
```

### Using Postman

1. Create a new POST request to `http://localhost:5000/api/parse`
2. Go to "Body" → "form-data"
3. Add key `file` with type `File` and select your PDF
4. Optional: Add key `issuer` with value like "Chase"
5. Send the request

### Using cURL

```bash
# Health check
curl http://localhost:5000/health

# Get supported issuers
curl http://localhost:5000/api/issuers

# Parse a statement
curl -X POST http://localhost:5000/api/parse \
  -F "file=@path/to/statement.pdf"
```

## 📁 Project Structure

```
Sure_Finance/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .env                       # Your environment variables (create this)
│
├── services/
│   └── pdf_parser.py          # PDF parsing service
│
├── utils/
│   ├── patterns.py            # Regex patterns for data extraction
│   └── helpers.py             # Helper functions
│
├── uploads/                   # Temporary PDF storage (auto-created)
│
└── README.md                  # This file
```

## 🔧 Configuration

Edit `.env` file to customize:

- `DEBUG`: Enable/disable debug mode (True/False)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 5000)
- `UPLOAD_FOLDER`: Folder for temporary file storage
- `MAX_CONTENT_LENGTH`: Max file size in bytes (default: 16MB)
- `DELETE_AFTER_PARSE`: Auto-delete files after parsing (True/False)

## 🛠️ Development

### Adding Support for New Issuers

1. Add issuer patterns in `utils/patterns.py`
2. Update `SUPPORTED_ISSUERS` in `config.py`
3. Add issuer detection logic in `services/pdf_parser.py`

### Customizing Data Extraction

Modify the extraction methods in `services/pdf_parser.py`:
- `_extract_card_number()`
- `_extract_billing_cycle()`
- `_extract_due_date()`
- etc.

## 📝 Error Handling

The API returns appropriate HTTP status codes:

- `200`: Success
- `400`: Bad request (invalid file, missing parameters)
- `404`: Endpoint not found
- `500`: Server error

Error response format:
```json
{
  "status": "error",
  "message": "Error description",
  "code": 400
}
```

## 🎯 Data Points Extracted

1. **Card Issuer**: Identifies the credit card company
2. **Card Last 4 Digits**: Last 4 digits of the card number
3. **Billing Cycle**: Start and end dates of the billing period
4. **Payment Due Date**: Date by which payment must be made
5. **Total Balance**: Current balance on the card
6. **Minimum Payment**: Minimum amount due
7. **Statement Date**: Date the statement was generated
8. **Account Holder**: Name on the account
9. **Credit Limit**: Maximum credit available
10. **Available Credit**: Remaining credit available

## 🔒 Security Considerations

- Files are sanitized using `secure_filename()`
- Temporary files are deleted after processing (if configured)
- No sensitive data is logged
- CORS is enabled (configure as needed for production)

## 📊 Confidence Scoring

The API provides an extraction confidence score:
- **High**: 80%+ of fields extracted
- **Medium**: 50-79% of fields extracted
- **Low**: <50% of fields extracted

## 🚀 Production Deployment

For production:

1. Set `DEBUG=False` in `.env`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set up proper logging
4. Configure CORS appropriately
5. Use environment variables for secrets
6. Set up file size limits
7. Implement rate limiting

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📄 License

This project is for the hackathon assignment.

## 👥 Support

For issues or questions, please contact the development team.

---

**Built with ❤️ for Sure Finance Hackathon**
