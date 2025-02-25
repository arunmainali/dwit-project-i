import tkinter as tk
from tkinter import ttk

def button_func():
	print(string_var.get())
	string_var.set("Button pressed")

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar(value = 'start value')

# widgets
label = ttk.Label(master = window, text = 'This is a label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise
# create 2 entry fields and 1 label, they should all be connected via StringVar
# set a start value of 'test

ex_string_var = tk.StringVar(value = 'test')

ex_entry1 = ttk.Entry(master = window, textvariable = ex_string_var)
ex_entry1.pack()
ex_entry2 = ttk.Entry(master = window, textvariable = ex_string_var)
ex_entry2.pack()

ex_label = ttk.Label(master = window, text = 'ex_label', textvariable = ex_string_var)
ex_label.pack()

# run
window.mainloop()
