import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        # Set light mode colors
        self.root.configure(bg="#ffffff")
        
        # Configure style
        self.setup_styles()
        
        # Create main frame with light background
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        self.create_widgets()
    
    def setup_styles(self):
        """Configure custom styles for the interface"""
        style = ttk.Style()
        
        # Set light theme
        style.theme_use('clam')
        
        # Configure colors for light mode
        style.configure(".", 
                       background="#ffffff",
                       foreground="#000000",
                       fieldbackground="#ffffff",
                       selectbackground="#0078d4",
                       selectforeground="#ffffff")
        
        # Title styling
        style.configure("Title.TLabel", 
                       font=("Arial", 16, "bold"),
                       background="#ffffff",
                       foreground="#2c5aa0")
        
        # Header styling
        style.configure("Header.TLabel", 
                       font=("Arial", 10, "bold"),
                       background="#ffffff",
                       foreground="#333333")
        
        # Button styling
        style.configure("TButton",
                       background="#f0f0f0",
                       foreground="#000000",
                       borderwidth=1,
                       focuscolor="#0078d4")
        
        # Entry styling
        style.configure("TEntry",
                       fieldbackground="#ffffff",
                       foreground="#000000",
                       borderwidth=1,
                       insertcolor="#000000")
        
        # Frame styling
        style.configure("TLabelframe",
                       background="#ffffff",
                       foreground="#333333",
                       borderwidth=1,
                       relief="solid")
        
        style.configure("TLabelframe.Label",
                       background="#ffffff",
                       foreground="#2c5aa0",
                       font=("Arial", 9, "bold"))
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Title
        title_label = ttk.Label(self.main_frame, text="Password Generator", style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Password length section
        length_frame = ttk.LabelFrame(self.main_frame, text="Password Length", padding="10")
        length_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(length_frame, text="Length:").grid(row=0, column=0, sticky=tk.W)
        
        self.length_var = tk.StringVar(value="12")
        length_spinbox = ttk.Spinbox(length_frame, from_=4, to=50, width=10, textvariable=self.length_var)
        length_spinbox.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)
        
        # Character options section
        options_frame = ttk.LabelFrame(self.main_frame, text="Character Options", padding="10")
        options_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.lowercase_var).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.uppercase_var).grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="Numbers (0-9)", variable=self.numbers_var).grid(row=0, column=1, sticky=tk.W, pady=2, padx=(20, 0))
        ttk.Checkbutton(options_frame, text="Special (!@#$%^&*)", variable=self.special_var).grid(row=1, column=1, sticky=tk.W, pady=2, padx=(20, 0))
        
        # Generate button with custom styling
        generate_btn = ttk.Button(self.main_frame, text="Generate Password", command=self.generate_password)
        generate_btn.grid(row=3, column=0, columnspan=2, pady=(0, 15))
        
        # Configure generate button for prominence
        style = ttk.Style()
        style.configure("Generate.TButton",
                       background="#0078d4",
                       foreground="#ffffff",
                       font=("Arial", 10, "bold"),
                       padding=(10, 5))
        generate_btn.configure(style="Generate.TButton")
        
        # Password display section
        password_frame = ttk.LabelFrame(self.main_frame, text="Generated Password", padding="10")
        password_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(password_frame, textvariable=self.password_var, 
                                      font=("Courier", 12), state="readonly", width=40)
        self.password_entry.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Configure password entry styling
        style = ttk.Style()
        style.configure("Password.TEntry",
                       fieldbackground="#f8f9fa",
                       foreground="#333333",
                       font=("Courier", 12),
                       borderwidth=2,
                       relief="solid")
        self.password_entry.configure(style="Password.TEntry")
        
        # Action buttons with enhanced styling
        copy_btn = ttk.Button(password_frame, text="📋 Copy to Clipboard", command=self.copy_password)
        copy_btn.grid(row=1, column=0, padx=(0, 5), sticky=tk.W)
        
        clear_btn = ttk.Button(password_frame, text="🗑️ Clear", command=self.clear_password)
        clear_btn.grid(row=1, column=1, padx=(5, 0), sticky=tk.E)
        
        # Configure action button styling
        style.configure("Action.TButton",
                       background="#f8f9fa",
                       foreground="#333333",
                       borderwidth=1,
                       padding=(8, 4))
        copy_btn.configure(style="Action.TButton")
        clear_btn.configure(style="Action.TButton")
        
        # Password strength indicator
        self.strength_var = tk.StringVar()
        self.strength_label = ttk.Label(self.main_frame, textvariable=self.strength_var, style="Header.TLabel")
        self.strength_label.grid(row=5, column=0, columnspan=2, pady=(0, 10))
        
        # Configure column weights
        password_frame.columnconfigure(0, weight=1)
        password_frame.columnconfigure(1, weight=1)
    
    def generate_password(self):
        """Generate password based on user selections"""
        try:
            # Validate inputs
            length = int(self.length_var.get())
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters.")
                return
            
            # Check if at least one option is selected
            if not any([self.lowercase_var.get(), self.uppercase_var.get(), 
                       self.numbers_var.get(), self.special_var.get()]):
                messagebox.showerror("Error", "Please select at least one character type.")
                return
            
            # Build character set
            char_set = ""
            guaranteed_chars = []
            
            if self.lowercase_var.get():
                char_set += string.ascii_lowercase
                guaranteed_chars.append(random.choice(string.ascii_lowercase))
            
            if self.uppercase_var.get():
                char_set += string.ascii_uppercase
                guaranteed_chars.append(random.choice(string.ascii_uppercase))
            
            if self.numbers_var.get():
                char_set += string.digits
                guaranteed_chars.append(random.choice(string.digits))
            
            if self.special_var.get():
                char_set += "!@#$%^&*"
                guaranteed_chars.append(random.choice("!@#$%^&*"))
            
            # Generate password
            password = guaranteed_chars.copy()
            remaining_length = length - len(guaranteed_chars)
            
            for _ in range(remaining_length):
                password.append(random.choice(char_set))
            
            # Shuffle password
            random.shuffle(password)
            final_password = ''.join(password)
            
            # Display password
            self.password_var.set(final_password)
            
            # Update strength indicator
            self.update_strength_indicator(final_password)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def update_strength_indicator(self, password):
        """Update password strength indicator"""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use 8+ characters")
        
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*" for c in password):
            score += 1
        
        if score <= 2:
            strength = "Weak"
            color = "#dc3545"  # Light red
        elif score <= 3:
            strength = "Medium"
            color = "#fd7e14"  # Light orange
        else:
            strength = "Strong"
            color = "#28a745"  # Light green
        
        self.strength_var.set(f"Password Strength: {strength}")
        self.strength_label.configure(foreground=color)
    
    def copy_password(self):
        """Copy password to clipboard"""
        password = self.password_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except:
                # Fallback if pyperclip is not available
                self.root.clipboard_clear()
                self.root.clipboard_append(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy. Generate a password first.")
    
    def clear_password(self):
        """Clear the password field"""
        self.password_var.set("")
        self.strength_var.set("")

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
