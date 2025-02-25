import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, size):
		super().__init__()

		# main setup
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0], size[1])

		# layout
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=5)
		self.rowconfigure(0, weight=1)

		# widget
		self.menu = toolbar_frame(self)
		self.menu.grid(row = 0, column = 0, sticky = tk.NSEW)

		# run
		self.mainloop()

class toolbar_frame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.create_widgets()
		self.create_layout()

	def create_widgets(self):
		self.menu_button1 = ttk.Button(self, text = 'Button 1')
		self.menu_button2 = ttk.Button(self, text = 'Button 2')
		self.menu_button3 = ttk.Button(self, text = 'Button 3')
		self.menu_button4 = ttk.Button(self, text = 'Button 4')

	def create_layout(self):
		# create the grid
		self.columnconfigure((0, 1), weight=1)
		self.rowconfigure((0, 1), weight=1)

		# place the widgets
		self.menu_button1.grid(row = 0, column = 0, sticky = 'nsew')
		self.menu_button2.grid(row = 0, column = 1, sticky = 'nsew')
		self.menu_button3.grid(row = 1, column = 0, sticky = 'nsew')
		self.menu_button4.grid(row = 1, column = 1, sticky = 'nsew')

App('Classes', (600, 600))
