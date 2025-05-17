# Employee Management System

A modular Python application for managing employee records through a graphical interface and SQLite database.

## Overview

This project demonstrates a clean separation of concerns with independent modules for data storage, business logic, user interface, and validation. It allows users to:

* **Create** new employee entries
* **Read** and display all existing records
* **Update** employee information
* **Delete** unwanted entries
* **Export** data to CSV, Excel, and PDF formats

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd employee_app
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
employee_app/              # Project root
├── db/                    # Database layer (SQLite operations)
│   ├── __init__.py
│   └── database.py        # Database class
├── models/                # Data models
│   ├── __init__.py
│   └── employee.py        # Employee dataclass
├── services/              # Business logic (CRUD)
│   ├── __init__.py
│   └── employee_service.py
├── ui/                    # Graphical interface (Tkinter)
│   ├── __init__.py
│   ├── employee_ui.py     # Main UI class
│   ├── add_employee_tab.py # Add/Edit employee tab
│   ├── view_employee_tab.py # View employees tab
│   └── export_utils.py    # Data export functionality
├── utils/                 # Validation and configuration
│   ├── __init__.py
│   ├── validators.py      # Input validation functions
│   └── config.py          # Constants and settings
├── app_config.json        # Application configuration file
├── main.py                # Application entry point
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## Usage

Run the application from the project root:

```bash
python main.py
```

Interact with the GUI to manage employee records. Data is automatically stored in `Employee.db` in the project folder.

### Features

1. **Add Employee Tab**: Create new employee records with validation
2. **View Employees Tab**: Browse, search, edit, and delete employee records
3. **Export Options**: Export employee data to CSV, Excel, or PDF formats

## Dependencies

The application requires the following external libraries:
- reportlab: For PDF generation
- openpyxl: For Excel generation

These dependencies are listed in the requirements.txt file.

## Future Improvements

* Implement user authentication
* Enhance search and filter functionality
* Add data visualization and reporting
* Package for PyPI distribution

---

Designed with a focus on modularity and maintainability.
