# tabs in tkinter
# we need to tk.Notebook widget
# tk.Notebook has some children (which are usually frames)
# Each frame is one tab

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Tabs')

# Notebook widget
notebook = ttk.Notebook(master = window)
# tabs

# NOTE: the parent doesn't have to be notebook. It can be anything.
# notebook seems the most sensible here
tab1 = ttk.Frame(master = notebook)
label1 = ttk.Label(master = tab1, text = 'Text in tab 1')
label1.pack()
button1 = ttk.Button(master = tab1, text = 'Button in tab 1')
button1.pack()

tab2 = ttk.Frame(master = notebook)
label2 = ttk.Label(master = tab2, text = 'Text in tab 2')
label2.pack()
entry2 = ttk.Entry(master = tab2)
entry2.pack()

# exercise
# add another tab with two buttons and one label inside
# run

tab3 = ttk.Frame(master = notebook)
button3_1 = ttk.Button(master = tab3, text = 'Button in tab 3')
button3_1.pack()
button3_2 = ttk.Button(master = tab3, text = 'Button in tab 3')
button3_2.pack()
label3 = ttk.Label(master = tab3, text = 'Text in tab 3')
label3.pack()

# NOTE: we do not pack frames using pack()
# instead we use notebook.add to "display" the frames
notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.add(tab3, text = 'Tab 3')

notebook.pack()

window.mainloop()
