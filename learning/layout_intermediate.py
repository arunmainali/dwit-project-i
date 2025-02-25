import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout Intermediate')
window.geometry('600x400')

# widgets
label1 = ttk.Label(master = window, text = 'Label 1', background = "red")
label2 = ttk.Label(master = window, text = 'Label 2', background = "blue")

# pack
# expand will make the widget take the entire available space
# label1.pack(side = 'left', expand = True, fill = 'x')
# label2.pack(side = 'left', expand = True, fill = 'both')

# grid
#window.columnconfigure(0, weight = 1)
#window.columnconfigure(1, weight = 1)
#window.columnconfigure(2, weight = 2)
#window.rowconfigure(0, weight = 1)
#window.rowconfigure(1, weight = 1)

# label only takes the minimal amount of space
# label1.grid(row = 0, column = 1)

#label1.grid(row = 0, column = 1, sticky = 'n')
#label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'n')

#label1.place(x = 0, y = 0, width = 200, height = 100)
#label2.place(relx = 0.3, rely = 0.5, relwidth = 1, anchor = 'center')

# run
window.mainloop()
