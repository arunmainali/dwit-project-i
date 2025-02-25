# to understand how parenting works
import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Layout Basics')

# frame
# tkinter window tries to have the size to fit the widgets inside it
frame = ttk.Frame(master = window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
# frame.pack_propagate(True)
frame.pack_propagate(False)
frame.pack(side = tk.LEFT)

# parenting (master setting)
# NOTE: ttk tries to set the size of a widget according to its children
# the size of the children overwrite the size of the parent
label = ttk.Label(master = frame, text = 'Label in frame')
label.pack()

button = ttk.Button(master = frame, text = 'Button in frame')
button.pack()

# example
label2 = ttk.Label(master = window, text = 'Label2 outside frame')
label2.pack()
# frame.pack()

# exercise
# create another frame with a label, a button, and an entry and place it to the right of the other widgets
ex_frame = ttk.Frame(master = window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
ex_frame.pack_propagate(True)
ex_frame.pack(side = tk.RIGHT)

ex_button = ttk.Button(master = ex_frame, text = 'Button in ex_frame')
ex_button.pack()

ex_label = ttk.Label(master = ex_frame, text = 'Label outside ex_frame')
ex_label.pack()

# run
window.mainloop()
