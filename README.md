"""
# Employee Management System

A modular Python application for managing employee records through a graphical interface and SQLite database.

## Overview

This project demonstrates a clean separation of concerns with independent modules for data storage, business logic, user interface, and validation. It allows users to:

* **Create** new employee entries
* **Read** and display all existing records
* **Update** employee information
* **Delete** unwanted entries

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
3. Install dependencies (none external; standard library only):

   ```bash
   pip install -r requirements.txt  # file can be empty or list only version pins
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
│   └── employee_ui.py     # UI class and layout
├── utils/                 # Validation and configuration
│   ├── __init__.py
│   ├── validators.py      # Input validation functions
│   └── config.py          # Constants and settings
├── main.py                # Application entry point
├── requirements.txt       # Dependencies (standard library)
└── README.md              # Project documentation
```

## Usage

Run the application from the project root:

```bash
python main.py
```

Interact with the GUI to manage employee records. Data is automatically stored in `Employee.db` in the project folder.

## Future Improvements

* Add reporting: export to CSV or PDF
* Implement user authentication
* Enhance search and filter functionality
* Package for PyPI distribution

---

Designed with a focus on modularity and maintainability.

"""