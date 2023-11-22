import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel

class MLGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Label Data")

        # Set the size of the window
        self.root.geometry("800x600")

        # Initialize data attribute
        self.loaded_data = None

        # Add your widgets here
        self.label = tk.Label(root, text="Select Data File:", font=("Helvetica", 14), fg='black')
        self.label.pack(pady=10)

        self.choose_file_button = tk.Button(root, text="Choose File", command=self.choose_file, font=("Helvetica", 12))
        self.choose_file_button.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.display_data_button = tk.Button(self.buttons_frame, text="Display Data", command=self.display_data, state=tk.DISABLED, font=("Helvetica", 12))
        self.display_data_button.grid(row=0, column=0, padx=10)

        self.run_ml_button = tk.Button(self.buttons_frame, text="Run ML Model", command=self.run_ml_model, state=tk.DISABLED, font=("Helvetica", 12))
        self.run_ml_button.grid(row=0, column=1, padx=10)

        # Text widget to display messages
        self.text_widget = tk.Text(root, height=10, width=80, font=("Helvetica", 12))
        self.text_widget.pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choose a data file", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.print_message(f"Selected file: {file_path}")

            # Load data and enable buttons
            self.loaded_data = self.load_data(file_path)
            if self.loaded_data is not None:
                self.enable_buttons()
                self.print_message(f"Data loaded successfully. Shape: {self.loaded_data.shape}")

    def load_data(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read().replace('\x00', '')  # Remove null characters
                data = pd.read_csv(file_path, encoding='latin-1')
            return data
        except Exception as e:
            self.print_message(f"Error loading data: {e}")
            return None

    def enable_buttons(self):
        self.display_data_button["state"] = tk.NORMAL
        self.run_ml_button["state"] = tk.NORMAL

    def display_data(self):
        if self.loaded_data is not None:
            data_display_window = tk.Toplevel(self.root)
            data_display_window.title("CSV Data Display")

            # Use PandasTable to display the data in a new window
            frame = tk.Frame(data_display_window)
            frame.pack(fill='both', expand=True)

            pt = Table(frame, dataframe=self.loaded_data, showtoolbar=True, showstatusbar=True)
            pt.show()

        else:
            self.print_message("No data loaded. Please choose a file first.")

    def run_ml_model(self):
        if self.loaded_data is not None:
            # Simulating ML model execution
            self.print_message("Running ML Model...")
            for i in range(5):
                self.print_message(f"Processing step {i + 1}...")
                self.root.update_idletasks()
                self.root.after(1000)  # Simulate processing time (1 second)
            self.print_message("ML Model completed.")
        else:
            self.print_message("No data loaded. Please choose a file first.")

    def print_message(self, message):
        self.text_widget.insert(tk.END, f"{message}\n")
        self.text_widget.see(tk.END)  # Scroll to the end of the text widget

if __name__ == "__main__":
    root = tk.Tk()
    app = MLGUI(root)
    root.mainloop()
