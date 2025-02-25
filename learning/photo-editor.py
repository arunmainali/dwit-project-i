import customtkinter as ctk

class App(ctk.CTk):
	def __init__(self):

		# setup
		super().__init__()
		self.geometry('1000x600')
		self.title('Photo Editor')
		self.minsize(800, 500)

		# layout
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=2)
		self.columnconfigure(1, weight=6)

		# widgets
		# import button

		# run
		self.mainloop()

App()
