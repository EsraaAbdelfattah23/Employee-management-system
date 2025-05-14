import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any, Optional, Callable
from services.employee_service import EmployeeService

class EmployeeUI:
    """
    User interface class for the Employee Management System.
    """
    def __init__(self, root: tk.Tk, employee_service: EmployeeService):
        """
        Initialize the UI components.
        
        Args:
            root: Tkinter root window
            employee_service: Service for employee operations
        """
        self.root = root
        self.service = employee_service
        self.selected_employee_id = None
        
        # Configure root window
        self.root.title('Employee Management System')
        self.root.geometry('1240x615+0+0')
        self.root.resizable(False, False)
        self.root.configure(bg='#40513B')
        
        # Initialize variables
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.job_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        
        # Create UI components
        self._create_logo()
        self._create_entries_frame()
        self._create_buttons()
        self._create_table_frame()
        
        # Load initial data
        self._display_all_employees()
    
    def _create_logo(self):
        """Create and place the logo"""
        try:
            self.logo = tk.PhotoImage(file='logo.png')
            lbl_logo = tk.Label(self.root, image=self.logo, bg='#40513B')
            lbl_logo.place(x=50, y=420)
        except tk.TclError:
            # If logo file is not found, show a placeholder
            lbl_logo = tk.Label(self.root, text="LOGO", font=('Calibri', 24), bg='#40513B', fg='white')
            lbl_logo.place(x=50, y=420)
    
    def _create_entries_frame(self):
        """Create and configure the entries frame"""
        # Create frame
        self.entries_frame = tk.Frame(self.root, bg='#40513B')
        self.entries_frame.place(x=1, y=1, width=360, height=510)
        
        # Title
        title = tk.Label(self.entries_frame, text='Employee Company', font=('Calibri', 16, 'bold'), bg='#40513B', fg='white')
        title.place(x=10, y=1)
        
        # Show/Hide buttons
        btn_hide = tk.Button(self.entries_frame, text='HIDE', bg='white', bd=1, relief=tk.SOLID, cursor='hand2', command=self._hide_sidebar)
        btn_hide.place(x=270, y=10)
        
        btn_show = tk.Button(self.entries_frame, text='SHOW', bg='white', bd=1, relief=tk.SOLID, cursor='hand2', command=self._show_sidebar)
        btn_show.place(x=310, y=10)
        
        # Name field
        tk.Label(self.entries_frame, text="Name", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=50)
        tk.Entry(self.entries_frame, textvariable=self.name_var, width=20, font=('Calibri', 12)).place(x=120, y=50)
        
        # Job field
        tk.Label(self.entries_frame, text="Job", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=90)
        tk.Entry(self.entries_frame, textvariable=self.job_var, width=20, font=('Calibri', 12)).place(x=120, y=90)
        
        # Gender field
        tk.Label(self.entries_frame, text="Gender", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=130)
        gender_combo = ttk.Combobox(self.entries_frame, textvariable=self.gender_var, state='readonly', width=18, font=('Calibri', 12))
        gender_combo['values'] = ("Male", "Female")
        gender_combo.place(x=120, y=130)
        
        # Age field
        tk.Label(self.entries_frame, text="Age", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=170)
        tk.Entry(self.entries_frame, textvariable=self.age_var, width=20, font=('Calibri', 12)).place(x=120, y=170)
        
        # Email field
        tk.Label(self.entries_frame, text="Email", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=210)
        tk.Entry(self.entries_frame, textvariable=self.email_var, width=20, font=('Calibri', 12)).place(x=120, y=210)
        
        # Phone field
        tk.Label(self.entries_frame, text="Phone no", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=250)
        tk.Entry(self.entries_frame, textvariable=self.phone_var, width=20, font=('Calibri', 12)).place(x=120, y=250)
        
        # Address field
        tk.Label(self.entries_frame, text="Address", font=('Calibri', 14), bg='#40513B', fg='white').place(x=10, y=290)
        self.address_text = tk.Text(self.entries_frame, width=30, height=2, font=('Calibri', 13), bg='white', fg='black')
        self.address_text.place(x=10, y=330)
    
    def _create_buttons(self):
        """Create and configure action buttons"""
        btn_frame = tk.Frame(self.entries_frame, bg='#40513B', relief=tk.SOLID)
        btn_frame.place(x=10, y=400, width=335, height=100)
        
        # Add button
        tk.Button(
            btn_frame,
            text='Add Details',
            width=14,
            height=1,
            font=('Calibri', 16),
            fg='white',
            bg='#3674B5',
            bd=0,
            command=self._add_employee
        ).place(x=4, y=5)
        
        # Update button
        tk.Button(
            btn_frame,
            text='Update Details',
            width=14,
            height=1,
            font=('Calibri', 16),
            fg='white',
            bg='#89A8B2',
            bd=0,
            command=self._update_employee
        ).place(x=4, y=50)
        
        # Delete button
        tk.Button(
            btn_frame,
            text='Delete Details',
            width=14,
            height=1,
            font=('Calibri', 16),
            fg='white',
            bg='#D84040',
            bd=0,
            command=self._delete_employee
        ).place(x=170, y=5)
        
        # Clear button
        tk.Button(
            btn_frame,
            text='Clear Details',
            width=14,
            height=1,
            font=('Calibri', 16),
            fg='white',
            bg='#8EA3A6',
            bd=0,
            command=self._clear_form
        ).place(x=170, y=50)
    
    def _create_table_frame(self):
        """Create and configure the table frame"""
        tree_frame = tk.Frame(self.root, bg='white')
        tree_frame.place(x=365, y=1, width=875, height=610)
        
        # Configure treeview style
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=50)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))
        
        # Create treeview
        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
        
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
        self.tv.place(x=1, y=1, height=610, width=875)
    
    def _get_selected_row(self, event):
        """Handle row selection in the treeview"""
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        if 'values' in data and data['values']:
            row = data["values"]
            self.selected_employee_id = row[0]
            
            # Fill form with selected employee data
            self.name_var.set(row[1])
            self.age_var.set(row[2])
            self.job_var.set(row[3])
            self.email_var.set(row[4])
            self.gender_var.set(row[5])
            self.phone_var.set(row[6])
            
            self.address_text.delete(1.0, tk.END)
            self.address_text.insert(tk.END, row[7])
    
    def _display_all_employees(self):
        """Display all employees in the treeview"""
        # Clear existing items
        self.tv.delete(*self.tv.get_children())
        
        # Fetch and display employees
        for row in self.service.get_all_employees():
            self.tv.insert("", tk.END, values=row)
    
    def _get_form_data(self) -> Dict[str, Any]:
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
    
    def _add_employee(self):
        """Add a new employee"""
        # Get form data
        employee_data = self._get_form_data()
        
        # Add employee through service
        success, message, _ = self.service.add_employee(employee_data)
        
        # Show result message
        if success:
            messagebox.showinfo("Success", message)
            self._clear_form()
            self._display_all_employees()
        else:
            messagebox.showerror("Error", message)
    
    def _update_employee(self):
        """Update the selected employee"""
        if not self.selected_employee_id:
            messagebox.showerror("Error", "Please select an employee to update")
            return
        
        # Get form data
        employee_data = self._get_form_data()
        
        # Update employee through service
        success, message = self.service.update_employee(self.selected_employee_id, employee_data)
        
        # Show result message
        if success:
            messagebox.showinfo("Success", message)
            self._clear_form()
            self._display_all_employees()
        else:
            messagebox.showerror("Error", message)
    
    def _delete_employee(self):
        """Delete the selected employee"""
        if not self.selected_employee_id:
            messagebox.showerror("Error", "Please select an employee to delete")
            return
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this employee?"):
            # Delete employee through service
            success, message = self.service.delete_employee(self.selected_employee_id)
            
            # Show result message
            if success:
                messagebox.showinfo("Success", message)
                self._clear_form()
                self._display_all_employees()
            else:
                messagebox.showerror("Error", message)
    
    def _clear_form(self):
        """Clear all form fields"""
        self.name_var.set("")
        self.age_var.set("")
        self.job_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.address_text.delete(1.0, tk.END)
        self.selected_employee_id = None
    
    def _hide_sidebar(self):
        """Hide the sidebar"""
        self.root.geometry("360x615+0+0")
    
    def _show_sidebar(self):
        """Show the sidebar"""
        self.root.geometry("1240x615+0+0")
