from tkinter import *
import customtkinter as ctk
from image_widgets import *

class App(ctk.CTk):
	def __init__(self):

		# setup
		super().__init__()
		ctk.set_apprearance_mode('dark')
		self.geometry('1000x600')
		self.title('Photo Editor')
		self.minsize(800, 500)

		# layout
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 2)
		self.columnconfigure(1, weight = 6)

		# widgets
		# ImportButton (Frame with a button)
		ImageImport(self)

		# run
		run.mainloop()

App()

# root = Tk()
# root.title("Paint App")
# root.geometry("1100x600")
#
# toolBar = Frame(root, height = 100, width = 1100, bg ="red")
# toolBar.grid(row = 0, column = 0)
#
# frame2 = Frame(root, height = 500, width = 1100, bg = "yellow")
# frame2.grid(row = 1, column = 0)
#
# canvas = Canvas(frame2, height = 500, width = 1100, bg = "white")
# canvas.grid(row = 0, column = 0)
#
# # canvas.create_line(100, 100, 200, 200)
# canvas.create_rectangle(100, 100, 200, 200)
# canvas.create_oval(100, 100, 200, 200)
#
# def paint(event):
# 	x = event.x
# 	y = event.y
# 	canvas.create_line(x, y, 100, 200, 200, fill = "black")
#
# canvas.bind("<Button-1>", paint)
#
# root.resizable(False, False)
#
# root.mainloop()
