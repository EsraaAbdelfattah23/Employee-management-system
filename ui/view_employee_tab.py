import tkinter as tk
from tkinter import ttk, messagebox

class ViewEmployeeTab:
    """Class for the View Employees tab functionality."""

    def __init__(self, parent, ui_instance):
        """
        Initialize the View Employees tab.

        Args:
            parent: Parent notebook
            ui_instance: Main UI instance for accessing shared resources
        """
        self.parent = parent
        self.ui = ui_instance

        # Create tab
        self.tab = ttk.Frame(parent)
        parent.add(self.tab, text='View Employees')

        # Setup tab content
        self._setup_tab()

    def _setup_tab(self):
        """Setup the View Employees tab content"""
        frame = ttk.Frame(self.tab, padding="20 20 20 20")
        frame.pack(fill='both', expand=True)

        # Search and export section
        self._create_search_export_section(frame)

        # Treeview for employee data
        self._create_employee_treeview(frame)

        # Action buttons
        self._create_action_buttons(frame)

    def _create_search_export_section(self, parent):
        """Create search bar and export button"""
        search_frame = ttk.Frame(parent)
        search_frame.pack(fill='x', pady=(0, 10))

        # Search field
        ttk.Label(search_frame, text="Search:", font=('Calibri', 12)).pack(side=tk.LEFT, padx=(0, 10))
        search_entry = ttk.Entry(search_frame, textvariable=self.ui.search_var, width=40, font=('Calibri', 12))
        search_entry.pack(side=tk.LEFT)

        # Bind search function to search variable
        self.ui.search_var.trace("w", self._on_search_change)

        # Export button
        export_button = ttk.Button(
            search_frame,
            text='Export Data',
            width=15,
            command=self._show_export_menu
        )
        export_button.pack(side=tk.RIGHT)

    def _create_employee_treeview(self, parent):
        """Create treeview for displaying employee data"""
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill='both', expand=True)

        # Create treeview with scrollbar
        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8))

        # Configure columns
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40)

        self.tv.heading("2", text="Name")
        self.tv.column("2", width=140)

        self.tv.heading("3", text="Age")
        self.tv.column("3", width=50)

        self.tv.heading("4", text="Job")
        self.tv.column("4", width=120)

        self.tv.heading("5", text="Email")
        self.tv.column("5", width=150)

        self.tv.heading("6", text="Gender")
        self.tv.column("6", width=90)

        self.tv.heading("7", text="Phone")
        self.tv.column("7", width=150)

        self.tv.heading("8", text="Address")
        self.tv.column("8", width=150)

        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self._get_selected_row)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=scrollbar.set)

        # Pack treeview and scrollbar
        self.tv.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.pack(side=tk.RIGHT, fill='y')

    def _create_action_buttons(self, parent):
        """Create action buttons for employee management"""
        action_frame = ttk.Frame(parent)
        action_frame.pack(fill='x', pady=(10, 0))

        # Edit button - switches to add tab for editing
        ttk.Button(
            action_frame,
            text='Edit Selected',
            width=20,
            command=self._switch_to_edit
        ).pack(side=tk.LEFT, padx=(0, 10))

        # Delete button
        ttk.Button(
            action_frame,
            text='Delete Selected',
            width=20,
            command=self._delete_employee
        ).pack(side=tk.LEFT)

    def _get_selected_row(self, event):
        """Handle row selection in the treeview"""
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        if 'values' in data and data['values']:
            row = data["values"]
            self.ui.selected_employee_id = row[0]

            # Fill form with selected employee data without switching tabs
            self.ui.name_var.set(row[1])
            self.ui.age_var.set(row[2])
            self.ui.job_var.set(row[3])
            self.ui.email_var.set(row[4])
            self.ui.gender_var.set(row[5])
            self.ui.phone_var.set(row[6])

            self.ui.address_text.delete(1.0, tk.END)
            self.ui.address_text.insert(tk.END, row[7])

            # Enable update button and disable add button
            self.ui.add_tab.update_btn.state(['!disabled'])
            self.ui.add_tab.add_btn.state(['disabled'])

    def _on_search_change(self, *args):
        """Handle search field changes"""
        search_text = self.ui.search_var.get().lower()
        self._filter_employees(search_text)

    def _filter_employees(self, search_text):
        """Filter employees based on search text"""
        # Clear existing items
        self.tv.delete(*self.tv.get_children())

        # Fetch all employees
        success, message, all_employees = self.ui.service.get_all_employees()

        if not success:
            messagebox.showerror("Error", message)
            return

        # Filter and display matching employees
        for row in all_employees:
            # Check if search text is in ID or name (case insensitive)
            if (search_text in str(row[0]).lower() or
                search_text in str(row[1]).lower()):
                self.tv.insert("", tk.END, values=row)

    def _switch_to_edit(self):
        """Switch to Add Employee tab for editing"""
        if not self.ui.selected_employee_id:
            messagebox.showerror("Error", "Please select an employee to edit")
            return

        # Switch to add tab
        self.ui.notebook.select(self.ui.add_tab.tab)

    def _delete_employee(self):
        """Delete the selected employee"""
        if not self.ui.selected_employee_id:
            messagebox.showerror("Error", "Please select an employee to delete")
            return

        # Get employee for confirmation
        success, message, employee = self.ui.service.get_employee_by_id(self.ui.selected_employee_id)
        if not success or not employee:
            messagebox.showerror("Error", message or "Failed to retrieve employee details")
            return

        # Confirm deletion with employee details
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete this employee?\nID: {self.ui.selected_employee_id}\nName: {employee.name}"
        )
        if not confirm:
            return

        # Delete employee through service
        success, message, _ = self.ui.service.delete_employee(self.ui.selected_employee_id)

        # Show result message
        if success:
            messagebox.showinfo("Success", message)
            self.ui.add_tab._clear_form()
            self.display_employees()
        else:
            messagebox.showerror("Error", message)

    def _show_export_menu(self):
        """Show export options menu"""
        # Create popup menu
        export_menu = tk.Menu(self.ui.root, tearoff=0)
        export_menu.add_command(label="Export to CSV", command=self.ui.export_utils.export_to_csv)
        export_menu.add_command(label="Export to Excel", command=self.ui.export_utils.export_to_excel)
        export_menu.add_command(label="Export to PDF", command=self.ui.export_utils.export_to_pdf)

        # Display popup menu
        try:
            export_menu.tk_popup(
                self.ui.root.winfo_pointerx(),
                self.ui.root.winfo_pointery()
            )
        finally:
            export_menu.grab_release()

    def display_employees(self):
        """Display all employees in the treeview"""
        # Clear existing items
        self.tv.delete(*self.tv.get_children())

        # Fetch all employees
        success, message, employees = self.ui.service.get_all_employees()

        if not success:
            messagebox.showerror("Error", message)
            return

        # Display employees in treeview
        for row in employees:
            self.tv.insert("", tk.END, values=row)
