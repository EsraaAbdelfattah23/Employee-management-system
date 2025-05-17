import unittest
from utils.validators import validate_email, validate_phone, validate_employee_data

class TestValidators(unittest.TestCase):
    """Test cases for validator functions."""
    
    def test_validate_email_valid(self):
        """Test validate_email with valid email addresses."""
        valid_emails = [
            "test@example.com",
            "user.name@domain.com",
            "user-name@domain.co.uk",
            "user123@domain.net",
            "user+tag@domain.org"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))
    
    def test_validate_email_invalid(self):
        """Test validate_email with invalid email addresses."""
        invalid_emails = [
            "test@",
            "@example.com",
            "test@.com",
            "test@example.",
            "test@exam ple.com",
            "test@exam\nple.com",
            "test"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))
    
    def test_validate_phone_valid(self):
        """Test validate_phone with valid phone numbers."""
        valid_phones = [
            "1234567890",
            "123-456-7890",
            "(123) 456-7890",
            "123 456 7890",
            "123-456-7890"
        ]
        
        for phone in valid_phones:
            with self.subTest(phone=phone):
                self.assertTrue(validate_phone(phone))
    
    def test_validate_phone_invalid(self):
        """Test validate_phone with invalid phone numbers."""
        invalid_phones = [
            "123",  # Too short
            "12345678901234567890",  # Too long
            "123-456-789a",  # Contains letters
            "123@456@7890",  # Contains special characters
            "123-456-789"  # Too short
        ]
        
        for phone in invalid_phones:
            with self.subTest(phone=phone):
                self.assertFalse(validate_phone(phone))
    
    def test_validate_employee_data_valid(self):
        """Test validate_employee_data with valid employee data."""
        valid_data = {
            'name': 'John Doe',
            'age': '30',
            'job': 'Developer',
            'email': 'john@example.com',
            'gender': 'Male',
            'phone': '123-456-7890',
            'address': '123 Main St, City, Country'
        }
        
        is_valid, message = validate_employee_data(valid_data)
        self.assertTrue(is_valid)
        self.assertEqual(message, "")
    
    def test_validate_employee_data_missing_fields(self):
        """Test validate_employee_data with missing fields."""
        # Test each required field
        required_fields = ['name', 'age', 'job', 'email', 'gender', 'phone', 'address']
        
        for field in required_fields:
            with self.subTest(field=field):
                # Create data with one field missing
                data = {
                    'name': 'John Doe',
                    'age': '30',
                    'job': 'Developer',
                    'email': 'john@example.com',
                    'gender': 'Male',
                    'phone': '123-456-7890',
                    'address': '123 Main St, City, Country'
                }
                data.pop(field)
                
                is_valid, message = validate_employee_data(data)
                self.assertFalse(is_valid)
                self.assertEqual(message, f"Field '{field}' is required")
    
    def test_validate_employee_data_invalid_email(self):
        """Test validate_employee_data with invalid email."""
        data = {
            'name': 'John Doe',
            'age': '30',
            'job': 'Developer',
            'email': 'invalid-email',
            'gender': 'Male',
            'phone': '123-456-7890',
            'address': '123 Main St, City, Country'
        }
        
        is_valid, message = validate_employee_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid email format")
    
    def test_validate_employee_data_invalid_phone(self):
        """Test validate_employee_data with invalid phone."""
        data = {
            'name': 'John Doe',
            'age': '30',
            'job': 'Developer',
            'email': 'john@example.com',
            'gender': 'Male',
            'phone': '123',  # Too short
            'address': '123 Main St, City, Country'
        }
        
        is_valid, message = validate_employee_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid phone number format")
    
    def test_validate_employee_data_non_numeric_age(self):
        """Test validate_employee_data with non-numeric age."""
        data = {
            'name': 'John Doe',
            'age': 'thirty',  # Non-numeric
            'job': 'Developer',
            'email': 'john@example.com',
            'gender': 'Male',
            'phone': '123-456-7890',
            'address': '123 Main St, City, Country'
        }
        
        is_valid, message = validate_employee_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Age must be a number")

if __name__ == '__main__':
    unittest.main()
