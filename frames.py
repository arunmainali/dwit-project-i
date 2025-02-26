import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class ToolbarFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.load_images()
		self.create_widgets()
		self.create_layout()

	def load_images(self):
		self.paint_brush_image = ctk.CTkImage(Image.open('images/paint-brush.png'))
		self.eraser_image = ctk.CTkImage(Image.open('images/eraser.png'))
		self.rectangle_image = ctk.CTkImage(Image.open('images/rectangle.png'))
		self.ellipse_image = ctk.CTkImage(Image.open('images/ellipse.png'))
		self.curve_line_image = ctk.CTkImage(Image.open('images/curve-line.png'))
		self.straight_line_image = ctk.CTkImage(Image.open('images/straight-line.png'))

	def create_widgets(self):
		self.paint_brush_button = ctk.CTkButton(self, image = self.paint_brush_image, text = '')
		self.eraser_button = ctk.CTkButton(self, image = self.eraser_image, text = '')
		self.rectangle_button = ctk.CTkButton(self, image = self.rectangle_image, text = '')
		self.ellipse_button = ctk.CTkButton(self, image = self.ellipse_image, text = '')
		self.curve_line_button = ctk.CTkButton(self, image = self.curve_line_image, text = '')
		self.straight_line_button = ctk.CTkButton(self, image = self.straight_line_image, text = '')

	def create_layout(self):
		# create the grid
		self.columnconfigure((0, 1), weight=1)
		self.rowconfigure((0, 1, 2), weight=1)

		# place the widgets
		self.paint_brush_button.grid(row = 0, column = 0)
		self.eraser_button.grid(row = 0, column = 1)
		self.rectangle_button.grid(row = 1, column = 0)
		self.ellipse_button.grid(row = 1, column = 1)
		self.curve_line_button.grid(row = 2, column = 0)
		self.straight_line_button.grid(row = 2, column = 1)

class CanvasFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.create_widgets()
		self.create_layout()

	def create_widgets(self):
		self.canvas = tk.Canvas(self, bg = 'white')

	def create_layout(self):
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

		self.canvas.grid(row = 0, column = 0, sticky = 'nsew')
