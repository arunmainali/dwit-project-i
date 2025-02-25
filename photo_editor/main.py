import customtkinter as ctk
from image_widths import *
from PIL import Image

class App(ctk.CTk):
	def __init__(self):

		# setup window
		super().__init__()
		self.geometry('400x400')
		self.title('Photo Editor')
		self.minsize(400, 400)

		# layout
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 2)
		self.columnconfigure(1, weight = 6)

		# widgets
		# importButton (Frame with a button)
		ImageImport(self, self.import_image)

		# run
		self.mainloop()

	def import_image(self, path):
		print(path)

App()
