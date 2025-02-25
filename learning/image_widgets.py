import customtkinter as ctk

class ImageImport(ctk.CTkFrame):
	# cover the entire window
	# it should contain a single button in the middle
	# the button should say "open image"
	def __init__(self, parent):
		super().__init__(master = parent)
		self.grid(column = 0, cloumnspan = 2, row = 0, sticky = 'nsew')

		ctk.CTkButton(self, text = 'open image').pack(expand = True)
