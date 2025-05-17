import tkinter as tk
from tkinter import filedialog, messagebox

class ExportUtils:
    """Utility class for exporting employee data to different formats."""

    def __init__(self, ui_instance):
        """
        Initialize export utilities.

        Args:
            ui_instance: Main UI instance for accessing shared resources
        """
        self.ui = ui_instance

    def export_to_csv(self):
        """Export employee data to CSV format"""
        # Ask user for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Export to CSV"
        )

        if not filename:
            return  # User cancelled

        # Call service to export data
        success, message, _ = self.ui.service.export_to_csv(filename)

        # Show result message
        if success:
            messagebox.showinfo("Export Successful", message)
        else:
            messagebox.showerror("Export Failed", message)

    def export_to_excel(self):
        """Export employee data to Excel format"""
        # Ask user for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Export to Excel"
        )

        if not filename:
            return  # User cancelled

        # Call service to export data
        success, message, _ = self.ui.service.export_to_excel(filename)

        # Show result message
        if success:
            messagebox.showinfo("Export Successful", message)
        else:
            messagebox.showerror("Export Failed", message)

    def export_to_pdf(self):
        """Export employee data to PDF format"""
        # Ask user for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            title="Export to PDF"
        )

        if not filename:
            return  # User cancelled

        # Call service to export data
        success, message, _ = self.ui.service.export_to_pdf(filename)

        # Show result message
        if success:
            messagebox.showinfo("Export Successful", message)
        else:
            messagebox.showerror("Export Failed", message)