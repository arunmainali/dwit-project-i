import tkinter as tk
from tkinter import ttk

def button_function():
	print('A button was pressed.')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('500x500')

# tk text
text = tk.Text(master = window)
text.pack()

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_function)
button.pack()

# exercise
# add one more text label and a button with a function that prints 'hello'
# the label should say my label and be between the entry widget and the button

def say_hello():
	print('Hello')

label_exc = ttk.Label(master = window, text = 'This is the label for the exercise')
label_exc.pack()

# button_exc = ttk.Button(master = window, text = 'Press me to say hello', command = say_hello)
button_exc = ttk.Button(master = window, text = 'Press me to say hello', command = lambda: print('Hello'))
button_exc.pack()

# run
window.mainloop()
