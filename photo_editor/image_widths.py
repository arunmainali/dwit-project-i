import customtkinter as ctk
from tkinter import filedialog

class ImageImport(ctk.CTkFrame):
	# cover the entire window
	# should contain a single button right in the middle
	# the button should say open image
	def __init__(self, parent, import_func):
		super().__init__(master = parent)
		self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
		self.import_func = import_func

		ctk.CTkButton(self, text = 'Open Image', command = self.open_dialog).pack(expand = True)

	def open_dialog(self):
		path = filedialog.askopenfile()
		self.import_func(path)
