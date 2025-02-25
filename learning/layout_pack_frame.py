import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack Parenting')
window.geometry('400x600')

# top frame
top_frame = ttk.Frame(master = window)
label1 = ttk.Label(master = top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(master = top_frame, text = 'Second label', background = 'blue')

# middle widget
label3 = ttk.Label(master = window, text = 'Third label', background = 'green')
label4 = ttk.Label(master = window, text = 'Fourth label', background = 'orange')
button1 = ttk.Button(master = window, text = 'A button')
button2 = ttk.Button(master = window, text = 'Another button')

# top layout
label1.pack(side = 'left', fill = 'both')
label2.pack(side = 'left', fill = 'both')
top_frame.pack(fill = 'both', expand = True)

# run
window.mainloop()
