# pack stacks widgets
# side = which side the widgets are added to
# expand = determines the vertical or horizontal space a widget *can* occupy
# fill = how much space the widget *will* occupy
# padding
# padx or pady (outside)
# ipadx or ipady (inside)

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack Layout')
window.geometry('400x600')

# widgets
label1 = ttk.Label(master = window, text = 'First Label', background = 'red')
label2 = ttk.Label(master = window, text = 'Second Label', background = 'blue')
label3 = ttk.Label(master = window, text = 'Third Label', background = 'green')
button = ttk.Button(master = window, text = 'Button')

# layout
# widgets will, by default, take the minimum space
#label1.pack(side = 'left', expand = True, fill = "both")
#label2.pack(side = 'left')
#label3.pack(side = 'left')
#button.pack(side = 'left', expand = True)

# exercise layout
label1.pack(side = 'top', fill = 'both')
label2.pack(side = 'top', expand = True, fill = 'none')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', fill = 'x')


# run
window.mainloop()
