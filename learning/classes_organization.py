# Key Idea:
# We take a tkinter widget via inheritance and add widgets to it

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, geometry):

		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{geometry[0]}x{geometry[1]}')
		self.minsize(geometry[0], geometry[1])

		# widgets
		self.menu = Menu(self)

		# run
		self.mainloop()

class Menu(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		ttk.Label(self, background = 'red').pack(expand = True, fill = 'both')
		self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

	def create_widgets(self):
		menu_button1 = ttk.Button(self, text = 'Button 1')

App('Class Based App', (600, 600))
