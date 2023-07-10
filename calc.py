import tkinter as tk
from tkinter import ttk

def calculate(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Invalid operation."

    result_label.config(text=str(result))

root = tk.Tk()
root.title("Calculator")

style = ttk.Style()
style.configure("TButton",
                foreground="midnight blue",
                background="light sky blue",
                font=("Arial", 16),
                padding=10)
style.configure("TEntry",
                foreground="midnight blue",
                font=("Arial", 16),
                padding=10)
style.configure("TLabel",
                foreground="midnight blue",
                background="alice blue",
                font=("Arial", 16),
                padding=10)

label1 = ttk.Label(root, text="Enter first number: ")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = ttk.Label(root, text="Enter second number: ")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

add_button = ttk.Button(root, text='+', command=lambda: calculate('+'))
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = ttk.Button(root, text='-', command=lambda: calculate('-'))
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = ttk.Button(root, text='*', command=lambda: calculate('*'))
multiply_button.grid(row=3, column=0, padx=10, pady=10)

divide_button = ttk.Button(root, text='/', command=lambda: calculate('/'))
divide_button.grid(row=3, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
