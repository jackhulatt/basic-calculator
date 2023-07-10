import tkinter as tk

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

label1 = tk.Label(root, text="Enter first number: ")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number: ")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text='+', command=lambda: calculate('+'))
add_button.pack()

subtract_button = tk.Button(root, text='-', command=lambda: calculate('-'))
subtract_button.pack()

multiply_button = tk.Button(root, text='*', command=lambda: calculate('*'))
multiply_button.pack()

divide_button = tk.Button(root, text='/', command=lambda: calculate('/'))
divide_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
