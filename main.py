import tkinter as tk
from db.database import Database
from services.employee_service import EmployeeService
from ui.employee_ui import EmployeeUI

def main():
    """
    Main entry point for the Employee Management System application.
    """
    # Create the root window
    root = tk.Tk()
    
    # Initialize database
    db = Database("Employee.db")
    
    # Initialize service with database
    employee_service = EmployeeService(db)
    
    # Initialize UI with root window and service
    app = EmployeeUI(root, employee_service)
    
    # Start the application
    root.mainloop()
    
    # Close database connection when application exits
    db.close()

if __name__ == "__main__":
    main()
