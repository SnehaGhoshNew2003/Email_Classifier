import re

def mask_pii(text):
    masked_entities = []
    original_text = text

    patterns = {
        'full_name': r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
        'email': r'\b[\w\.-]+@[\w\.-]+\.\w+\b',
        'phone_number': r'\b\d{10,12}\b',
        'dob': r'\b\d{2}[\/\-]\d{2}[\/\-]\d{4}\b',
        'aadhar_num': r'\b\d{12}\b',
        'credit_debit_no': r'\b\d{13,16}\b',
        'cvv_no': r'\b\d{3}\b',
        'expiry_no': r'\b(0[1-9]|1[0-2])\/?([0-9]{2})\b'
    }

    masked_text = text
    for entity, pattern in patterns.items():
        for match in re.finditer(pattern, original_text):
            start, end = match.span()
            entity_value = match.group()
            masked_text = masked_text.replace(entity_value, f"[{entity}]")
            masked_entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": entity_value
            })
    return masked_text, masked_entities

def preprocess_email(text):
    # Very basic cleaning
    text = text.lower()
    return text
