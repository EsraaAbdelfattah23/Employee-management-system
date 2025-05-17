import tkinter as tk
from db.database import Database
from services.employee_service import EmployeeService
from ui.employee_ui import EmployeeUI
from utils.config import AppConfig

def main():
    """
    Main entry point for the Employee Management System application.
    """
    # Load configuration
    config = AppConfig()

    # Create the root window
    root = tk.Tk()

    # Initialize database with path from config
    db = None

    try:
        # Get database path from config
        db_path = config.get_db_path()

        # Initialize database
        db = Database(db_path)

        # Initialize service with database
        employee_service = EmployeeService(db)

        # Initialize UI with root window, service, and config
        app = EmployeeUI(root, employee_service, config)

        # Start the application
        root.mainloop()
    finally:
        # Close database connection when application exits
        if db:
            db.close()

if __name__ == "__main__":
    main()
