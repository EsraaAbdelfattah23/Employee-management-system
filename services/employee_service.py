from typing import List, Tuple, Dict, Any, Optional
from models.employee import Employee
from db.database import Database
from utils.validators import validate_employee_data

class EmployeeService:
    """
    Service class for employee-related business logic.
    """
    def __init__(self, database: Database):
        """
        Initialize the employee service with a database connection.
        
        Args:
            database: Database instance for data operations
        """
        self.db = database
        
    def add_employee(self, employee_data: Dict[str, Any]) -> Tuple[bool, str, Optional[int]]:
        """
        Add a new employee to the database after validation.
        
        Args:
            employee_data: Dictionary containing employee data
            
        Returns:
            Tuple of (success, message, employee_id)
        """
        # Validate employee data
        is_valid, error_message = validate_employee_data(employee_data)
        if not is_valid:
            return False, error_message, None
        
        # Create employee object
        employee = Employee(
            name=employee_data['name'],
            age=employee_data['age'],
            job=employee_data['job'],
            email=employee_data['email'],
            gender=employee_data['gender'],
            phone=employee_data['phone'],
            address=employee_data['address']
        )
        
        # Insert into database
        employee_id = self.db.insert_employee(employee)
        return True, "Employee added successfully", employee_id
    
    def update_employee(self, employee_id: int, employee_data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Update an existing employee after validation.
        
        Args:
            employee_id: ID of the employee to update
            employee_data: Dictionary containing updated employee data
            
        Returns:
            Tuple of (success, message)
        """
        # Validate employee data
        is_valid, error_message = validate_employee_data(employee_data)
        if not is_valid:
            return False, error_message
        
        # Create employee object with ID
        employee = Employee(
            id=employee_id,
            name=employee_data['name'],
            age=employee_data['age'],
            job=employee_data['job'],
            email=employee_data['email'],
            gender=employee_data['gender'],
            phone=employee_data['phone'],
            address=employee_data['address']
        )
        
        # Update in database
        success = self.db.update_employee(employee)
        if success:
            return True, "Employee updated successfully"
        else:
            return False, "Failed to update employee"
    
    def delete_employee(self, employee_id: int) -> Tuple[bool, str]:
        """
        Delete an employee from the database.
        
        Args:
            employee_id: ID of the employee to delete
            
        Returns:
            Tuple of (success, message)
        """
        success = self.db.remove_employee(employee_id)
        if success:
            return True, "Employee deleted successfully"
        else:
            return False, "Failed to delete employee"
    
    def get_all_employees(self) -> List[Tuple]:
        """
        Get all employees from the database.
        
        Returns:
            List of tuples containing employee data
        """
        return self.db.fetch_all_employees()
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """
        Get an employee by ID.
        
        Args:
            employee_id: ID of the employee to retrieve
            
        Returns:
            Employee object if found, None otherwise
        """
        employees = self.db.fetch_all_employees()
        for emp in employees:
            if emp[0] == employee_id:
                return Employee.from_tuple(emp)
        return None
