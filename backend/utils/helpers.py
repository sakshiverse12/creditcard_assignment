"""
Helper functions for data extraction and cleaning
"""

import re
from datetime import datetime
from typing import Optional


def clean_text(text: str) -> str:
    """
    Clean extracted text by removing extra whitespace and special characters
    
    Args:
        text: Raw text to clean
    
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove non-printable characters
    text = ''.join(char for char in text if char.isprintable() or char in '\n\r\t')
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def extract_amount(amount_str: str) -> Optional[str]:
    """
    Extract and format monetary amount from string
    
    Args:
        amount_str: String containing amount (e.g., "$1,234.56" or "1234.56")
    
    Returns:
        Formatted amount as string (e.g., "1234.56") or None if invalid
    """
    if not amount_str:
        return None
    
    # Remove currency symbols, commas, and extra whitespace
    cleaned = re.sub(r'[$,\s]', '', amount_str)
    
    # Extract numeric value (including decimals)
    match = re.search(r'(\d+\.?\d{0,2})', cleaned)
    if match:
        amount = match.group(1)
        # Format to 2 decimal places
        try:
            return f"{float(amount):.2f}"
        except ValueError:
            return None
    
    return None


def parse_date(date_str: str) -> Optional[str]:
    """
    Parse date string and return in standardized format
    
    Args:
        date_str: Date string in various formats
    
    Returns:
        Date in YYYY-MM-DD format or None if parsing fails
    """
    if not date_str:
        return None
    
    # Clean the date string
    date_str = clean_text(date_str)
    
    # Common date formats to try
    date_formats = [
        '%m/%d/%Y',
        '%m/%d/%y',
        '%m-%d-%Y',
        '%m-%d-%y',
        '%B %d, %Y',
        '%b %d, %Y',
        '%B %d %Y',
        '%b %d %Y',
        '%d/%m/%Y',
        '%d/%m/%y',
        '%Y-%m-%d',
    ]
    
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    # If no format matches, try to extract date components
    # Pattern: MM/DD/YYYY or similar
    match = re.search(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})', date_str)
    if match:
        month, day, year = match.groups()
        # Convert 2-digit year to 4-digit
        if len(year) == 2:
            year = f"20{year}" if int(year) < 50 else f"19{year}"
        
        try:
            date_obj = datetime(int(year), int(month), int(day))
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            pass
    
    return None


def format_currency(amount: float) -> str:
    """
    Format amount as currency string
    
    Args:
        amount: Numeric amount
    
    Returns:
        Formatted currency string (e.g., "$1,234.56")
    """
    return f"${amount:,.2f}"


def validate_card_last4(digits: str) -> bool:
    """
    Validate that the string contains exactly 4 digits
    
    Args:
        digits: String to validate
    
    Returns:
        True if valid last 4 digits, False otherwise
    """
    if not digits:
        return False
    
    return bool(re.match(r'^\d{4}$', digits))
