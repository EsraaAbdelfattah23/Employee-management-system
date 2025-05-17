import unittest
import os
import sqlite3
from db.database import Database
from services.employee_service import EmployeeService
from models.employee import Employee

class TestEmployeeService(unittest.TestCase):
    """Test cases for EmployeeService class."""
    
    def setUp(self):
        """Set up test environment before each test."""
        # Use in-memory database for testing
        self.db = Database(":memory:")
        self.service = EmployeeService(self.db)
        
        # Add some test data
        self.test_employee_data = {
            'name': 'John Doe',
            'age': '30',
            'job': 'Developer',
            'email': 'john@example.com',
            'gender': 'Male',
            'phone': '123-456-7890',
            'address': '123 Main St, City, Country'
        }
    
    def tearDown(self):
        """Clean up after each test."""
        self.db.close()
    
    def test_add_employee_valid(self):
        """Test adding a valid employee."""
        # Add employee
        success, message, employee_id = self.service.add_employee(self.test_employee_data)
        
        # Check result
        self.assertTrue(success)
        self.assertEqual(message, "Employee added successfully")
        self.assertIsNotNone(employee_id)
        
        # Verify employee was added to database
        success, _, employees = self.service.get_all_employees()
        self.assertTrue(success)
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0][1], self.test_employee_data['name'])
    
    def test_add_employee_invalid(self):
        """Test adding an invalid employee."""
        # Create invalid data (missing required field)
        invalid_data = self.test_employee_data.copy()
        invalid_data.pop('name')
        
        # Try to add employee
        success, message, employee_id = self.service.add_employee(invalid_data)
        
        # Check result
        self.assertFalse(success)
        self.assertEqual(message, "Field 'name' is required")
        self.assertIsNone(employee_id)
        
        # Verify no employee was added to database
        success, _, employees = self.service.get_all_employees()
        self.assertTrue(success)
        self.assertEqual(len(employees), 0)
    
    def test_update_employee(self):
        """Test updating an employee."""
        # Add employee
        success, _, employee_id = self.service.add_employee(self.test_employee_data)
        self.assertTrue(success)
        
        # Update employee
        updated_data = self.test_employee_data.copy()
        updated_data['name'] = 'Jane Doe'
        updated_data['age'] = '35'
        
        success, message, updated_id = self.service.update_employee(employee_id, updated_data)
        
        # Check result
        self.assertTrue(success)
        self.assertEqual(message, "Employee updated successfully")
        self.assertEqual(updated_id, employee_id)
        
        # Verify employee was updated in database
        success, _, employees = self.service.get_all_employees()
        self.assertTrue(success)
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0][1], 'Jane Doe')
        self.assertEqual(employees[0][2], '35')
    
    def test_delete_employee(self):
        """Test deleting an employee."""
        # Add employee
        success, _, employee_id = self.service.add_employee(self.test_employee_data)
        self.assertTrue(success)
        
        # Delete employee
        success, message, deleted_id = self.service.delete_employee(employee_id)
        
        # Check result
        self.assertTrue(success)
        self.assertEqual(message, "Employee deleted successfully")
        self.assertEqual(deleted_id, employee_id)
        
        # Verify employee was deleted from database
        success, _, employees = self.service.get_all_employees()
        self.assertTrue(success)
        self.assertEqual(len(employees), 0)
    
    def test_get_employee_by_id(self):
        """Test getting an employee by ID."""
        # Add employee
        success, _, employee_id = self.service.add_employee(self.test_employee_data)
        self.assertTrue(success)
        
        # Get employee by ID
        success, message, employee = self.service.get_employee_by_id(employee_id)
        
        # Check result
        self.assertTrue(success)
        self.assertEqual(message, "Employee found")
        self.assertIsNotNone(employee)
        self.assertEqual(employee.id, employee_id)
        self.assertEqual(employee.name, self.test_employee_data['name'])
        self.assertEqual(employee.age, self.test_employee_data['age'])
        self.assertEqual(employee.job, self.test_employee_data['job'])
        self.assertEqual(employee.email, self.test_employee_data['email'])
        self.assertEqual(employee.gender, self.test_employee_data['gender'])
        self.assertEqual(employee.phone, self.test_employee_data['phone'])
        self.assertEqual(employee.address, self.test_employee_data['address'])
    
    def test_get_employee_by_id_not_found(self):
        """Test getting a non-existent employee by ID."""
        # Get employee by non-existent ID
        success, message, employee = self.service.get_employee_by_id(999)
        
        # Check result
        self.assertFalse(success)
        self.assertEqual(message, "Employee with ID 999 not found")
        self.assertIsNone(employee)
    
    def test_get_all_employees(self):
        """Test getting all employees."""
        # Initially, there should be no employees
        success, _, employees = self.service.get_all_employees()
        self.assertTrue(success)
        self.assertEqual(len(employees), 0)
        
        # Add some employees
        self.service.add_employee(self.test_employee_data)
        
        second_employee = self.test_employee_data.copy()
        second_employee['name'] = 'Jane Doe'
        second_employee['email'] = 'jane@example.com'
        self.service.add_employee(second_employee)
        
        # Get all employees
        success, message, employees = self.service.get_all_employees()
        
        # Check result
        self.assertTrue(success)
        self.assertEqual(message, "Employees retrieved successfully")
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0][1], 'John Doe')
        self.assertEqual(employees[1][1], 'Jane Doe')

if __name__ == '__main__':
    unittest.main()
