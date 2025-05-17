import tkinter as tk
from tkinter import ttk, messagebox

class AddEmployeeTab:
    """Class for the Add Employee tab functionality."""

    def __init__(self, parent, ui_instance):
        """
        Initialize the Add Employee tab.

        Args:
            parent: Parent notebook
            ui_instance: Main UI instance for accessing shared resources
        """
        self.parent = parent
        self.ui = ui_instance

        # Create tab
        self.tab = ttk.Frame(parent)
        parent.add(self.tab, text='Add Employee')

        # Setup tab content
        self._setup_tab()

    def _setup_tab(self):
        """Setup the Add Employee tab content"""
        frame = ttk.Frame(self.tab, padding="20 20 20 20")
        frame.pack(fill='both', expand=True)

        # Create form fields
        self._create_form_fields(frame)

        # Create action buttons
        self._create_action_buttons(frame)

    def _create_form_fields(self, parent):
        """Create form fields for employee data entry"""
        # Create a frame for the form
        form_frame = ttk.Frame(parent)
        form_frame.pack(fill='both', expand=True)

        # Configure grid layout
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=2)
        form_frame.columnconfigure(2, weight=1)
        form_frame.columnconfigure(3, weight=2)

        # Name field
        ttk.Label(form_frame, text="Name:", font=('Calibri', 12)).grid(row=0, column=0, sticky='w', padx=5, pady=10)
        ttk.Entry(form_frame, textvariable=self.ui.name_var, width=30, font=('Calibri', 12)).grid(row=0, column=1, sticky='w', padx=5, pady=10)

        # Age field
        ttk.Label(form_frame, text="Age:", font=('Calibri', 12)).grid(row=0, column=2, sticky='w', padx=5, pady=10)
        ttk.Entry(form_frame, textvariable=self.ui.age_var, width=30, font=('Calibri', 12)).grid(row=0, column=3, sticky='w', padx=5, pady=10)

        # Job field
        ttk.Label(form_frame, text="Job:", font=('Calibri', 12)).grid(row=1, column=0, sticky='w', padx=5, pady=10)
        ttk.Entry(form_frame, textvariable=self.ui.job_var, width=30, font=('Calibri', 12)).grid(row=1, column=1, sticky='w', padx=5, pady=10)

        # Gender field
        ttk.Label(form_frame, text="Gender:", font=('Calibri', 12)).grid(row=1, column=2, sticky='w', padx=5, pady=10)
        gender_frame = ttk.Frame(form_frame)
        gender_frame.grid(row=1, column=3, sticky='w', padx=5, pady=10)

        ttk.Radiobutton(gender_frame, text="Male", variable=self.ui.gender_var, value="Male").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(gender_frame, text="Female", variable=self.ui.gender_var, value="Female").pack(side=tk.LEFT)

        # Email field
        ttk.Label(form_frame, text="Email:", font=('Calibri', 12)).grid(row=2, column=0, sticky='w', padx=5, pady=10)
        ttk.Entry(form_frame, textvariable=self.ui.email_var, width=30, font=('Calibri', 12)).grid(row=2, column=1, sticky='w', padx=5, pady=10)

        # Phone field
        ttk.Label(form_frame, text="Phone:", font=('Calibri', 12)).grid(row=2, column=2, sticky='w', padx=5, pady=10)
        ttk.Entry(form_frame, textvariable=self.ui.phone_var, width=30, font=('Calibri', 12)).grid(row=2, column=3, sticky='w', padx=5, pady=10)

        # Address field
        ttk.Label(form_frame, text="Address:", font=('Calibri', 12)).grid(row=3, column=0, sticky='nw', padx=5, pady=10)

        # Create Text widget for address
        self.ui.address_text = tk.Text(form_frame, width=62, height=5, font=('Calibri', 12))
        self.ui.address_text.grid(row=3, column=1, columnspan=3, sticky='w', padx=5, pady=10)

    def _create_action_buttons(self, parent):
        """Create action buttons for adding/updating employees"""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill='x', pady=(20, 0))

        # Add button
        self.add_btn = ttk.Button(
            button_frame,
            text='Add Employee',
            width=20,
            command=self._add_employee
        )
        self.add_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Update button (initially disabled)
        self.update_btn = ttk.Button(
            button_frame,
            text='Update Employee',
            width=20,
            command=self._update_employee,
            state='disabled'
        )
        self.update_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Clear button
        ttk.Button(
            button_frame,
            text='Clear Form',
            width=20,
            command=self._clear_form
        ).pack(side=tk.LEFT)

    def _add_employee(self):
        """Add a new employee"""
        # Get form data
        employee_data = self.ui.get_form_data()

        # Add employee through service
        success, message, _ = self.ui.service.add_employee(employee_data)

        # Show result message
        if success:
            messagebox.showinfo("Success", message)
            self._clear_form()
            self.ui._display_all_employees()
            # Switch to view tab
            self.ui.notebook.select(self.ui.view_tab.tab)
        else:
            messagebox.showerror("Error", message)

    def _update_employee(self):
        """Update the selected employee"""
        if not self.ui.selected_employee_id:
            messagebox.showerror("Error", "Please select an employee to update")
            return

        # Get form data
        employee_data = self.ui.get_form_data()

        # Update employee through service
        success, message, _ = self.ui.service.update_employee(self.ui.selected_employee_id, employee_data)

        # Show result message
        if success:
            messagebox.showinfo("Success", message)
            self._clear_form()
            self.ui._display_all_employees()
            # Switch to view tab
            self.ui.notebook.select(self.ui.view_tab.tab)
        else:
            messagebox.showerror("Error", message)

    def _clear_form(self):
        """Clear all form fields"""
        self.ui.name_var.set('')
        self.ui.age_var.set('')
        self.ui.job_var.set('')
        self.ui.gender_var.set('')
        self.ui.email_var.set('')
        self.ui.phone_var.set('')
        self.ui.address_text.delete(1.0, tk.END)

        # Reset selected employee
        self.ui.selected_employee_id = None

        # Enable add button and disable update button
        self.add_btn.state(['!disabled'])
        self.update_btn.state(['disabled'])
