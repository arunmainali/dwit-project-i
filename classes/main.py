import tkinter as tk
from tkinter import ttk

from frames import *

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
		self.menu = ToolbarFrame(self)
		self.menu.grid(row = 0, column = 0, sticky = tk.NSEW)

		# run
		self.mainloop()

App('Classes', (600, 600))
