import tkinter as tk
import math
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear_entry():
    entry.delete(0, tk.END)
def add_to_expression(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))
def calculate_square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def calculate_trigonometric_function(func):
    try:
        angle = float(entry.get())
        if func == 'sin':
            result = math.sin(math.radians(angle))
        elif func == 'cos':
            result = math.cos(math.radians(angle))
        elif func == 'tan':
            result = math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def calculate_logarithm():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
root = tk.Tk()
root.title("Scientific Calculator")
root.config(bg="black")
entry = tk.Entry(root, width=25, font=('Arial', 20), bd=5, insertwidth=4, justify='right', fg="white", bg="black")
entry.grid(row=0, column=0, columnspan=5)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
    ('tan', 6, 0), ('log', 6, 1)
]
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bd=8,
                       command=lambda t=text: add_to_expression(t) if t != '=' else evaluate_expression(),
                       fg="white", bg="orange" if not text.isdigit() else "gray22")
    button.grid(row=row, column=column)
sqrt_button = tk.Button(root, text='√', padx=20, pady=20, font=('Arial', 14), bd=8, command=calculate_square_root, fg="white", bg="gray22")
sqrt_button.grid(row=5, column=1)
sin_button = tk.Button(root, text='sin', padx=20, pady=20, font=('Arial', 14), bd=8, command=lambda: calculate_trigonometric_function('sin'), fg="white", bg="gray22")
sin_button.grid(row=5, column=2)
cos_button = tk.Button(root, text='cos', padx=20, pady=20, font=('Arial', 14), bd=8, command=lambda: calculate_trigonometric_function('cos'), fg="white", bg="gray22")
cos_button.grid(row=5, column=3)
tan_button = tk.Button(root, text='tan', padx=20, pady=20, font=('Arial', 14), bd=8, command=lambda: calculate_trigonometric_function('tan'), fg="white", bg="gray22")
tan_button.grid(row=6, column=0)
log_button = tk.Button(root, text='log', padx=20, pady=20, font=('Arial', 14), bd=8, command=calculate_logarithm, fg="white", bg="gray22")
log_button.grid(row=6, column=1)
root.mainloop()
