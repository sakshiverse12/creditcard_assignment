"""
Regex patterns for extracting data from credit card statements
"""

# Issuer-specific patterns
ISSUER_PATTERNS = {
    'Chase': {
        'card_number': [
            r'Account Number[:\s]+.*?(\d{4})',
            r'Card ending in[:\s]+(\d{4})',
        ],
        'billing_cycle': [
            r'Statement Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'due_date': [
            r'Payment Due Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
            r'Due Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'total_balance': [
            r'New Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
            r'Total Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'minimum_payment': [
            r'Minimum Payment Due[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'statement_date': [
            r'Statement Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
            r'Closing Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'account_holder': [
            r'(?:Account Holder|Name)[:\s]+([A-Z][a-zA-Z\s]+)',
        ],
        'credit_limit': [
            r'Credit Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'available_credit': [
            r'Available Credit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
    },
    'American Express': {
        'card_number': [
            r'Card Member[:\s]+.*?(\d{4})',
            r'Account ending in[:\s]+(\d{4})',
        ],
        'billing_cycle': [
            r'Statement Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*to\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'due_date': [
            r'Payment Due[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'total_balance': [
            r'Total Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
            r'New Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'minimum_payment': [
            r'Minimum Payment[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'statement_date': [
            r'Statement Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'account_holder': [
            r'Card Member[:\s]+([A-Z][a-zA-Z\s]+)',
        ],
        'credit_limit': [
            r'Credit Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'available_credit': [
            r'Available for Purchases[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
    },
    'Citibank': {
        'card_number': [
            r'Account Number[:\s]+.*?(\d{4})',
        ],
        'billing_cycle': [
            r'Statement Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'due_date': [
            r'Payment Due Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'total_balance': [
            r'New Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'minimum_payment': [
            r'Minimum Payment Due[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'statement_date': [
            r'Statement Closing Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'account_holder': [
            r'(?:Account Holder|Primary Cardholder)[:\s]+([A-Z][a-zA-Z\s]+)',
        ],
        'credit_limit': [
            r'Credit Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'available_credit': [
            r'Available Credit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
    },
    'Capital One': {
        'card_number': [
            r'Account Number[:\s]+.*?(\d{4})',
        ],
        'billing_cycle': [
            r'Statement Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'due_date': [
            r'Payment Due[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'total_balance': [
            r'New Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'minimum_payment': [
            r'Minimum Payment[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'statement_date': [
            r'Statement Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'account_holder': [
            r'(?:Account Holder|Name)[:\s]+([A-Z][a-zA-Z\s]+)',
        ],
        'credit_limit': [
            r'Credit Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'available_credit': [
            r'Available Credit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
    },
    'Discover': {
        'card_number': [
            r'Account Number[:\s]+.*?(\d{4})',
        ],
        'billing_cycle': [
            r'Statement Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'due_date': [
            r'Payment Due Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'total_balance': [
            r'New Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'minimum_payment': [
            r'Minimum Payment[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'statement_date': [
            r'Statement Closing Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        ],
        'account_holder': [
            r'(?:Account Holder|Name)[:\s]+([A-Z][a-zA-Z\s]+)',
        ],
        'credit_limit': [
            r'Credit Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
        'available_credit': [
            r'Credit Available[:\s]+\$?([\d,]+\.?\d{0,2})',
        ],
    },
}

# Common patterns that work across multiple issuers
COMMON_PATTERNS = {
    'card_number': [
        r'(?:Account|Card)(?:\s+Number)?[:\s]+.*?(\d{4})',
        r'ending in[:\s]+(\d{4})',
        r'(?:xxxx|XXXX)[:\s\-]*(\d{4})',
    ],
    'billing_cycle': [
        r'(?:Statement|Billing)\s+(?:Period|Cycle)[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*(?:-|to|through)\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        r'(\d{1,2}/\d{1,2}/\d{2,4})\s*(?:-|to)\s*(\d{1,2}/\d{1,2}/\d{2,4})',
    ],
    'due_date': [
        r'(?:Payment\s+)?Due\s+(?:Date|By)[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        r'Pay(?:ment)?\s+By[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
    ],
    'total_balance': [
        r'(?:New|Total|Current)\s+Balance[:\s]+\$?([\d,]+\.?\d{0,2})',
        r'Balance\s+Due[:\s]+\$?([\d,]+\.?\d{0,2})',
        r'Amount\s+Due[:\s]+\$?([\d,]+\.?\d{0,2})',
    ],
    'minimum_payment': [
        r'Minimum\s+Payment(?:\s+Due)?[:\s]+\$?([\d,]+\.?\d{0,2})',
        r'Min\.?\s+Payment[:\s]+\$?([\d,]+\.?\d{0,2})',
    ],
    'statement_date': [
        r'Statement\s+(?:Date|Closing\s+Date)[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
        r'Closing\s+Date[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})',
    ],
    'account_holder': [
        r'(?:Account\s+Holder|Card\s+Member|Name)[:\s]+([A-Z][a-zA-Z\s]{2,40})',
    ],
    'credit_limit': [
        r'Credit\s+Limit[:\s]+\$?([\d,]+\.?\d{0,2})',
        r'Total\s+Credit\s+Line[:\s]+\$?([\d,]+\.?\d{0,2})',
    ],
    'available_credit': [
        r'(?:Available|Credit\s+Available)[:\s]+\$?([\d,]+\.?\d{0,2})',
        r'Available\s+Credit[:\s]+\$?([\d,]+\.?\d{0,2})',
    ],
}
