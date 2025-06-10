import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 4:
        return ""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password_chars += random.choices(all_chars, k=length - 4)
    random.shuffle(password_chars)

    return ''.join(password_chars)

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

label_length = tk.Label(root, text="Enter Password Length (min 4):")
label_length.pack(pady=(20, 5))

entry_length = tk.Entry(root, width=10)
entry_length.pack()

btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.pack(pady=15)

label_password = tk.Label(root, text="Generated Password:")
label_password.pack()

entry_password = tk.Entry(root, width=40, justify='center')
entry_password.pack(pady=(5, 20))

root.mainloop()
