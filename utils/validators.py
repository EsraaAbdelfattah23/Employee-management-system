import re
from typing import Tuple, Dict, Any
from models.employee import Employee

def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email string to validate
        
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """
    Validate phone number format.
    
    Args:
        phone: Phone number string to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Allow digits, spaces, dashes, and parentheses
    pattern = r'^[0-9\s\-\(\)]{7,15}$'
    return bool(re.match(pattern, phone))

def validate_employee_data(employee_data: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validate employee data before saving.
    
    Args:
        employee_data: Dictionary containing employee data
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check for empty fields
    required_fields = ['name', 'age', 'job', 'email', 'gender', 'phone', 'address']
    for field in required_fields:
        if field not in employee_data or not employee_data[field]:
            return False, f"Field '{field}' is required"
    
    # Validate email format
    if not validate_email(employee_data['email']):
        return False, "Invalid email format"
    
    # Validate phone format
    if not validate_phone(employee_data['phone']):
        return False, "Invalid phone number format"
    
    # Validate age is numeric
    if not employee_data['age'].isdigit():
        return False, "Age must be a number"
    
    return True, ""
