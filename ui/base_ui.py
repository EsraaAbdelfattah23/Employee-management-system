import tkinter as tk
from tkinter import ttk
from services.employee_service import EmployeeService

class BaseUI:
    """Base class for the Employee Management System UI."""
    
    def __init__(self, root: tk.Tk, employee_service: EmployeeService):
        """
        Initialize the base UI components.
        
        Args:
            root: Tkinter root window
            employee_service: Service for employee operations
        """
        self.root = root
        self.service = employee_service
        self.selected_employee_id = None
        
        # Configure root window
        self._configure_root()
        
        # Initialize variables
        self._init_variables()
    
    def _configure_root(self):
        """Configure the root window properties"""
        self.root.title('Employee Management System')
        self.root.geometry('1240x615+0+0')
        self.root.resizable(True, True)
        self.root.configure(bg="#283149")
        
        # Apply custom theme
        self._apply_default_theme()
    
    def _init_variables(self):
        """Initialize Tkinter variables"""
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.job_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.search_var = tk.StringVar()
    
    def _apply_default_theme(self):
        """Apply custom theme to the application using the provided color palette"""
        # Color palette:
        # Dark Blue: #283149 (background, headers)
        # Medium Blue: #404B69 (secondary elements)
        # Teal: #00818A (buttons, highlights)
        # Light Blue: #DBEDF3 (light backgrounds)
        
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure main elements
        style.configure("TFrame", background="#DBEDF3")
        style.configure("TLabel", background="#DBEDF3", foreground="#283149")
        style.configure("TButton", padding=6, relief="flat", background="#00818A", foreground="white")
        
        # Configure notebook and tabs
        style.configure("TNotebook", background="#283149")
        style.configure("TNotebook.Tab", padding=[12, 4], background="#404B69", foreground="white", font=('Calibri', 10, 'bold'))
        style.map("TNotebook.Tab", background=[("selected", "#00818A")], foreground=[("selected", "white")])
        
        # Configure treeview
        style.configure("Treeview", background="white", foreground="#283149", fieldbackground="white", font=('Calibri', 10), rowheight=25)
        style.configure("Treeview.Heading", background="#404B69", foreground="white", font=('Calibri', 11, 'bold'))
        style.map("Treeview", background=[("selected", "#00818A")], foreground=[("selected", "white")])