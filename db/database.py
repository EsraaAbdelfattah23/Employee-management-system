import sqlite3
from typing import List, Tuple, Optional
from models.employee import Employee

class Database:
    """
    Database class for handling SQLite operations.
    """
    def __init__(self, db_path: str):
        """
        Initialize database connection and create tables if they don't exist.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

        # Create employees table if it doesn't exist
        sql = """
        CREATE TABLE IF NOT EXISTS Employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            job TEXT,
            email TEXT,
            gender TEXT,
            phone TEXT,
            address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert_employee(self, employee: Employee) -> int:
        """
        Insert a new employee record into the database.
        
        Args:
            employee: Employee object containing data to insert
            
        Returns:
            The ID of the newly inserted employee
        """
        self.cur.execute(
            "INSERT INTO Employees VALUES (NULL,?,?,?,?,?,?,?)",
            employee.to_tuple()
        )
        self.con.commit()
        return self.cur.lastrowid

    def fetch_all_employees(self) -> List[Tuple]:
        """
        Fetch all employee records from the database.
        
        Returns:
            List of tuples containing employee data
        """
        self.cur.execute("SELECT * FROM Employees")
        rows = self.cur.fetchall()
        return rows

    def remove_employee(self, employee_id: int) -> bool:
        """
        Remove an employee record from the database.
        
        Args:
            employee_id: ID of the employee to remove
            
        Returns:
            True if successful, False otherwise
        """
        self.cur.execute("DELETE FROM Employees WHERE id=?", (employee_id,))
        self.con.commit()
        return self.cur.rowcount > 0

    def update_employee(self, employee: Employee) -> bool:
        """
        Update an employee record in the database.
        
        Args:
            employee: Employee object containing updated data
            
        Returns:
            True if successful, False otherwise
        """
        if employee.id is None:
            return False
            
        self.cur.execute(
            "UPDATE Employees SET name=?, age=?, job=?, email=?, gender=?, phone=?, address=? WHERE id=?",
            employee.to_tuple()
        )
        self.con.commit()
        return self.cur.rowcount > 0
        
    def close(self):
        """Close the database connection"""
        if self.con:
            self.con.close()
