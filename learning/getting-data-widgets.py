import tkinter as tk
from tkinter import ttk

def button_func():
	# get the content of the entry
	print(entry.get())

	# update the label
	# label.configure(text = entry.get())
	label['text'] = entry.get()
	entry['state'] = 'disabled'

def exercise_button_func():
	label['text'] = 'some text'
	entry['state'] = 'disabled'

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'This is a label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Click Me', command = button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that disables entry

exercise_button = ttk.Button(master = window, text = 'disable entry', command = exercise_button_func)
exercise_button.pack()

# run
window.mainloop()
