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

		# configure layout
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=5)
		self.rowconfigure(0, weight=1)

		# widget
		self.canvas_frame = CanvasFrame(self, None)
		self.canvas_frame.grid(row = 0, column = 1, sticky = tk.NSEW)

		self.toolbar_frame = ToolbarFrame(self, self.canvas_frame)
		self.toolbar_frame.grid(row = 0, column = 0, sticky = tk.NSEW)

		# passing canvas_frame here to avoid circular dependency
		self.toolbar_frame.canvas_frame = self.canvas_frame

		# run
		self.mainloop()

App('Whiteboard', (600, 600))
