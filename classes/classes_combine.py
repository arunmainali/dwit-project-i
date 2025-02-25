import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, size):
		super().__init__()

		# main setup
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0], size[1])

		# widget
		self.menu = Menu(self)
		self.menu.pack()

		# run
		self.mainloop()

class Menu(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.create_widgets()
		self.create_layout()

	def create_widgets(self):
		self.menu_button1 = ttk.Button(self, text = 'Button 1')
		self.menu_button2 = ttk.Button(self, text = 'Button 1')
		self.menu_button3 = ttk.Button(self, text = 'Button 1')

		self.entry = ttk.Entry(self)

	def create_layout(self):
		# create the grid
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=5)
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)

		# place the widgets
		self.menu_button1.grid(row=0, column=0)
		self.menu_button2.grid(row=0, column=1)
		self.menu_button3.grid(row=1, column=2)

App('Classes', (600, 600))
