"""
PDF Parser Service
Handles extraction of data from credit card statements
"""

import re
import pdfplumber
import PyPDF2
from datetime import datetime
from typing import Dict, List, Optional, Any
import logging

from utils.patterns import ISSUER_PATTERNS, COMMON_PATTERNS
from utils.helpers import clean_text, extract_amount, parse_date


class PDFParserService:
    """Service for parsing credit card statement PDFs"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.supported_issuers = [
            'Chase',
            'American Express',
            'Citibank',
            'Capital One',
            'Discover'
        ]
    
    def get_supported_issuers(self) -> List[str]:
        """Return list of supported credit card issuers"""
        return self.supported_issuers
    
    def parse_statement(self, filepath: str, issuer_hint: Optional[str] = None) -> Dict[str, Any]:
        """
        Parse a credit card statement PDF and extract key data points
        
        Args:
            filepath: Path to the PDF file
            issuer_hint: Optional hint about which issuer (for optimization)
        
        Returns:
            Dictionary containing extracted data points
        """
        try:
            # Extract text from PDF
            text = self._extract_text_from_pdf(filepath)
            
            if not text or len(text.strip()) < 50:
                raise ValueError("Unable to extract text from PDF or PDF is empty")
            
            # Identify the issuer
            issuer = issuer_hint if issuer_hint else self._identify_issuer(text)
            
            # Extract data points
            data = {
                'card_issuer': issuer,
                'card_last_4_digits': self._extract_card_number(text, issuer),
                'billing_cycle': self._extract_billing_cycle(text, issuer),
                'payment_due_date': self._extract_due_date(text, issuer),
                'total_balance': self._extract_total_balance(text, issuer),
                'minimum_payment': self._extract_minimum_payment(text, issuer),
                'statement_date': self._extract_statement_date(text, issuer),
                'account_holder': self._extract_account_holder(text, issuer),
                'credit_limit': self._extract_credit_limit(text, issuer),
                'available_credit': self._extract_available_credit(text, issuer)
            }
            
            # Add metadata
            data['extraction_confidence'] = self._calculate_confidence(data)
            data['raw_text_length'] = len(text)
            
            return data
            
        except Exception as e:
            self.logger.error(f"Error parsing PDF: {str(e)}")
            raise Exception(f"Failed to parse statement: {str(e)}")
    
    def _extract_text_from_pdf(self, filepath: str) -> str:
        """Extract text from PDF using multiple methods"""
        text = ""
        
        # Try pdfplumber first (better for complex layouts)
        try:
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            self.logger.warning(f"pdfplumber extraction failed: {e}")
        
        # Fallback to PyPDF2 if pdfplumber fails
        if not text or len(text.strip()) < 50:
            try:
                with open(filepath, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    for page in pdf_reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
            except Exception as e:
                self.logger.error(f"PyPDF2 extraction also failed: {e}")
        
        return clean_text(text)
    
    def _identify_issuer(self, text: str) -> str:
        """Identify the credit card issuer from the text"""
        text_lower = text.lower()
        
        # Check for issuer-specific keywords
        if any(keyword in text_lower for keyword in ['chase', 'jpmorgan']):
            return 'Chase'
        elif any(keyword in text_lower for keyword in ['american express', 'amex']):
            return 'American Express'
        elif any(keyword in text_lower for keyword in ['citibank', 'citi card']):
            return 'Citibank'
        elif any(keyword in text_lower for keyword in ['capital one']):
            return 'Capital One'
        elif any(keyword in text_lower for keyword in ['discover']):
            return 'Discover'
        
        return 'Unknown'
    
    def _extract_card_number(self, text: str, issuer: str) -> Optional[str]:
        """Extract last 4 digits of card number"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('card_number', [])
        patterns.extend(COMMON_PATTERNS['card_number'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                # Extract just the last 4 digits
                card_num = match.group(1) if match.groups() else match.group(0)
                digits = re.findall(r'\d+', card_num)
                if digits:
                    last_4 = ''.join(digits)[-4:]
                    return last_4
        
        return None
    
    def _extract_billing_cycle(self, text: str, issuer: str) -> Optional[str]:
        """Extract billing cycle dates"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('billing_cycle', [])
        patterns.extend(COMMON_PATTERNS['billing_cycle'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                if match.groups():
                    start = match.group(1)
                    end = match.group(2) if len(match.groups()) > 1 else match.group(1)
                    return f"{parse_date(start)} to {parse_date(end)}"
                return match.group(0)
        
        return None
    
    def _extract_due_date(self, text: str, issuer: str) -> Optional[str]:
        """Extract payment due date"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('due_date', [])
        patterns.extend(COMMON_PATTERNS['due_date'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                date_str = match.group(1) if match.groups() else match.group(0)
                return parse_date(date_str)
        
        return None
    
    def _extract_total_balance(self, text: str, issuer: str) -> Optional[str]:
        """Extract total balance amount"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('total_balance', [])
        patterns.extend(COMMON_PATTERNS['total_balance'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                amount = match.group(1) if match.groups() else match.group(0)
                return extract_amount(amount)
        
        return None
    
    def _extract_minimum_payment(self, text: str, issuer: str) -> Optional[str]:
        """Extract minimum payment amount"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('minimum_payment', [])
        patterns.extend(COMMON_PATTERNS['minimum_payment'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                amount = match.group(1) if match.groups() else match.group(0)
                return extract_amount(amount)
        
        return None
    
    def _extract_statement_date(self, text: str, issuer: str) -> Optional[str]:
        """Extract statement date"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('statement_date', [])
        patterns.extend(COMMON_PATTERNS['statement_date'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                date_str = match.group(1) if match.groups() else match.group(0)
                return parse_date(date_str)
        
        return None
    
    def _extract_account_holder(self, text: str, issuer: str) -> Optional[str]:
        """Extract account holder name"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('account_holder', [])
        patterns.extend(COMMON_PATTERNS['account_holder'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                name = match.group(1) if match.groups() else match.group(0)
                return clean_text(name).title()
        
        return None
    
    def _extract_credit_limit(self, text: str, issuer: str) -> Optional[str]:
        """Extract credit limit"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('credit_limit', [])
        patterns.extend(COMMON_PATTERNS['credit_limit'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                amount = match.group(1) if match.groups() else match.group(0)
                return extract_amount(amount)
        
        return None
    
    def _extract_available_credit(self, text: str, issuer: str) -> Optional[str]:
        """Extract available credit"""
        patterns = ISSUER_PATTERNS.get(issuer, {}).get('available_credit', [])
        patterns.extend(COMMON_PATTERNS['available_credit'])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                amount = match.group(1) if match.groups() else match.group(0)
                return extract_amount(amount)
        
        return None
    
    def _calculate_confidence(self, data: Dict[str, Any]) -> str:
        """Calculate extraction confidence based on how many fields were found"""
        total_fields = len([k for k in data.keys() if not k.startswith('_')])
        extracted_fields = len([v for v in data.values() if v is not None and v != 'Unknown'])
        
        confidence_ratio = extracted_fields / total_fields if total_fields > 0 else 0
        
        if confidence_ratio >= 0.8:
            return 'high'
        elif confidence_ratio >= 0.5:
            return 'medium'
        else:
            return 'low'
