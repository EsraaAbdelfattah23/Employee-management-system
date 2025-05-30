import tkinter as tk
from tkinter import ttk, messagebox
from services.employee_service import EmployeeService
from ui.add_employee_tab import AddEmployeeTab
from ui.view_employee_tab import ViewEmployeeTab
from ui.export_utils import ExportUtils
from utils.config import AppConfig

class EmployeeUI:
    """
    User interface class for the Employee Management System.
    Provides a complete GUI for managing employee records.
    """
    def __init__(self, root: tk.Tk, employee_service: EmployeeService, config: AppConfig = None):
        """
        Initialize the UI components.

        Args:
            root: Tkinter root window
            employee_service: Service for employee operations
            config: Application configuration
        """
        self.root = root
        self.service = employee_service
        self.selected_employee_id = None
        self.address_text = None  # Will be initialized in AddEmployeeTab
        self.config = config or AppConfig()  # Use provided config or create a new one

        # Configure root window
        self._configure_root()

        # Initialize variables
        self._init_variables()

        # Initialize export utilities before creating menu
        self.export_utils = ExportUtils(self)

        # Create UI components
        self._create_menu()
        self._create_notebook()

        # Load initial data
        self._display_all_employees()

    def _configure_root(self):
        """Configure the root window properties"""
        self.root.title('Employee Management System')
        self.root.geometry('1240x615+0+0')
        self.root.resizable(True, True)

        # Get theme from config
        theme = self.config.get_theme()
        bg_color = "#283149" if theme == "Light" else "#1A1A2E"  # Default to Light theme color

        self.root.configure(bg=bg_color)

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
        # Address will be a Text widget, not a StringVar

    def _apply_default_theme(self):
        """Apply custom theme to the application using the provided color palette"""
        # Get theme from config
        theme = self.config.get_theme()

        # Define color schemes
        themes = {
            "Light": {
                "bg_primary": "#283149",       # Dark Blue (background, headers)
                "bg_secondary": "#404B69",     # Medium Blue (secondary elements)
                "accent": "#00818A",           # Teal (buttons, highlights)
                "bg_light": "#DBEDF3",         # Light Blue (light backgrounds)
                "text_dark": "#283149",        # Dark text
                "text_light": "white"          # Light text
            },
            "Dark": {
                "bg_primary": "#1A1A2E",       # Dark Navy (background, headers)
                "bg_secondary": "#16213E",     # Navy Blue (secondary elements)
                "accent": "#0F3460",           # Deep Blue (buttons, highlights)
                "bg_light": "#E2E2E2",         # Light Gray (light backgrounds)
                "text_dark": "#1A1A2E",        # Dark text
                "text_light": "#E2E2E2"        # Light text
            }
        }

        # Use Light theme as fallback if selected theme is not available
        colors = themes.get(theme, themes["Light"])

        style = ttk.Style()
        style.theme_use('clam')

        # Configure main elements
        style.configure("TFrame", background=colors["bg_light"])
        style.configure("TLabel", background=colors["bg_light"], foreground=colors["text_dark"])
        style.configure("TButton", padding=6, relief="flat", background=colors["accent"], foreground=colors["text_light"])

        # Configure notebook and tabs
        style.configure("TNotebook", background=colors["bg_primary"])
        style.configure("TNotebook.Tab", padding=[12, 4], background=colors["bg_secondary"],
                    foreground=colors["text_light"], font=('Calibri', 10, 'bold'))
        style.map("TNotebook.Tab", background=[("selected", colors["accent"])],
                foreground=[("selected", colors["text_light"])])

        # Configure treeview
        style.configure("Treeview", background="white", foreground=colors["text_dark"],
                       fieldbackground="white", font=('Calibri', 10), rowheight=25)
        style.configure("Treeview.Heading", background=colors["bg_secondary"],
                       foreground=colors["text_light"], font=('Calibri', 11, 'bold'))
        style.map("Treeview", background=[("selected", colors["accent"])],
                 foreground=[("selected", colors["text_light"])])

    def _create_menu(self):
        """Create application menu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)

        # Export submenu
        export_menu = tk.Menu(file_menu, tearoff=0)
        export_menu.add_command(label="Export to CSV", command=self.export_utils.export_to_csv)
        export_menu.add_command(label="Export to Excel", command=self.export_utils.export_to_excel)
        export_menu.add_command(label="Export to PDF", command=self.export_utils.export_to_pdf)

        file_menu.add_cascade(label="Export Data", menu=export_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def _create_notebook(self):
        """Create and setup the notebook with tabs"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Create tabs using separate classes
        self.add_tab = AddEmployeeTab(self.notebook, self)
        self.view_tab = ViewEmployeeTab(self.notebook, self)

    def _display_all_employees(self):
        """Display all employees in the treeview"""
        self.view_tab.display_employees()

    def _show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About",
            "Employee Management System\nVersion 1.0\n\nA modular Python application for managing employee records."
        )

    def get_form_data(self):
        """Get data from the form fields"""
        return {
            'name': self.name_var.get(),
            'age': self.age_var.get(),
            'job': self.job_var.get(),
            'email': self.email_var.get(),
            'gender': self.gender_var.get(),
            'phone': self.phone_var.get(),
            'address': self.address_text.get(1.0, tk.END).strip()
        }





