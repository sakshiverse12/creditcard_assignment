"""
Credit Card Statement Parser - Flask Backend
Main Application File
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import traceback

from services.pdf_parser import PDFParserService
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize services
parser_service = PDFParserService()

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET'])
def home():
    """API Home - Health Check"""
    return jsonify({
        'status': 'success',
        'message': 'Credit Card Statement Parser API',
        'version': '1.0.0',
        'endpoints': {
            'parse_statement': '/api/parse',
            'supported_issuers': '/api/issuers',
            'health': '/health'
        }
    }), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/issuers', methods=['GET'])
def get_supported_issuers():
    """Get list of supported credit card issuers"""
    issuers = parser_service.get_supported_issuers()
    return jsonify({
        'status': 'success',
        'supported_issuers': issuers,
        'count': len(issuers)
    }), 200


@app.route('/api/parse', methods=['POST'])
def parse_statement():
    """
    Parse credit card statement PDF
    
    Expected: multipart/form-data with 'file' field
    Optional: 'issuer' field to specify the credit card issuer
    
    Returns: Extracted data points from the statement
    """
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No file provided. Please upload a PDF file.'
            }), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No file selected.'
            }), 400
        
        # Check file extension
        if not allowed_file(file.filename):
            return jsonify({
                'status': 'error',
                'message': 'Invalid file type. Only PDF files are allowed.'
            }), 400
        
        # Get optional issuer parameter
        issuer_hint = request.form.get('issuer', None)
        
        # Save file securely
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        try:
            # Parse the PDF
            result = parser_service.parse_statement(filepath, issuer_hint)
            
            # Clean up uploaded file
            if app.config['DELETE_AFTER_PARSE']:
                os.remove(filepath)
            
            return jsonify({
                'status': 'success',
                'data': result,
                'filename': filename,
                'parsed_at': datetime.now().isoformat()
            }), 200
            
        except Exception as parse_error:
            # Clean up uploaded file on error
            if os.path.exists(filepath):
                os.remove(filepath)
            raise parse_error
            
    except Exception as e:
        app.logger.error(f"Error parsing statement: {str(e)}")
        app.logger.error(traceback.format_exc())
        
        return jsonify({
            'status': 'error',
            'message': f'Error processing statement: {str(e)}',
            'details': traceback.format_exc() if app.debug else None
        }), 500


@app.route('/api/batch-parse', methods=['POST'])
def batch_parse_statements():
    """
    Parse multiple credit card statement PDFs at once
    
    Expected: multipart/form-data with multiple 'files' field
    
    Returns: Array of extracted data from all statements
    """
    try:
        # Check if files are present
        if 'files' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No files provided. Please upload PDF files.'
            }), 400
        
        files = request.files.getlist('files')
        
        if len(files) == 0:
            return jsonify({
                'status': 'error',
                'message': 'No files selected.'
            }), 400
        
        results = []
        errors = []
        
        for file in files:
            if file.filename == '':
                continue
            
            if not allowed_file(file.filename):
                errors.append({
                    'filename': file.filename,
                    'error': 'Invalid file type'
                })
                continue
            
            try:
                # Save file
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
                unique_filename = f"{timestamp}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(filepath)
                
                # Parse
                result = parser_service.parse_statement(filepath)
                results.append({
                    'filename': filename,
                    'data': result,
                    'status': 'success'
                })
                
                # Clean up
                if app.config['DELETE_AFTER_PARSE']:
                    os.remove(filepath)
                    
            except Exception as e:
                errors.append({
                    'filename': file.filename,
                    'error': str(e)
                })
                if os.path.exists(filepath):
                    os.remove(filepath)
        
        return jsonify({
            'status': 'success',
            'parsed_count': len(results),
            'error_count': len(errors),
            'results': results,
            'errors': errors if errors else None,
            'parsed_at': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        app.logger.error(f"Error in batch parsing: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Error processing statements: {str(e)}'
        }), 500


def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'code': 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'code': 500
    }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("Credit Card Statement Parser API")
    print("=" * 60)
    print(f"Server running on: http://localhost:{app.config['PORT']}")
    print(f"Supported Issuers: {', '.join(parser_service.get_supported_issuers())}")
    print("=" * 60)
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
