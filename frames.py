import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class ToolbarFrame(tk.Frame):
	def __init__(self, parent, canvas_frame):
		super().__init__(parent)

		self.canvas_frame = canvas_frame

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
		self.paint_brush_button = ctk.CTkButton(self, image = self.paint_brush_image, text = '', command = self.canvas_frame.select_paint_brush)
		self.eraser_button = ctk.CTkButton(self, image = self.eraser_image, text = '', command = self.canvas_frame.select_eraser)
		self.rectangle_button = ctk.CTkButton(self, image = self.rectangle_image, text = '', command = self.canvas_frame.select_rectangle)
		self.ellipse_button = ctk.CTkButton(self, image = self.ellipse_image, text = '', command = self.canvas_frame.select_ellipse)
		self.curve_line_button = ctk.CTkButton(self, image = self.curve_line_image, text = '', command = self.canvas_frame.select_curve_line)
		self.straight_line_button = ctk.CTkButton(self, image = self.straight_line_image, text = '', command = self.canvas_frame.select_straight_line)

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

		self.tool = 'brush'
		self.stroke_color = 'black'
		self.fill_color = 'white'

		self.start_x = None
		self.start_y = None

		self.create_widgets()
		self.create_layout()

		self.canvas.bind('<Button-1>', self.on_button_press)
		self.canvas.bind('<Button1-Motion>', self.on_mouse_drag)
		self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

	def create_widgets(self):
		self.canvas = tk.Canvas(self, bg = 'white')

	def create_layout(self):
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

		self.canvas.grid(row = 0, column = 0, sticky = 'nsew')

	def select_paint_brush(self):
		self.tool = 'paint_brush'

	def select_eraser(self):
		self.tool = 'eraser'

	def select_rectangle(self):
		self.tool = 'rectangle'

	def select_curve_line(self):
		self.tool = 'curve_line'

	def select_straight_line(self):
		self.tool = 'straight_line'

	def select_ellipse(self):
		self.tool = 'ellipse'

	def clear_canvas(self):
		self.canvas.delete('all')

	def on_button_press(self, event):
		self.start_x = event.x
		self.start_y = event.y

	def on_mouse_drag(self, event):
		self.canvas.delete('preview')
		if self.tool == 'paint_brush':
			self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill = self.stroke_color, capstyle = tk.ROUND, smooth = True)
			self.start_x, self.start_y = event.x, event.y
		elif self.tool == 'eraser':
			self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill= 'white', capstyle=tk.ROUND, smooth=True)
			self.start_x, self.start_y = event.x, event.y
		elif self.tool == 'straight_line':
			self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill = self.stroke_color, tags = 'preview')
		elif self.tool == 'rectangle':
			self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline = self.stroke_color, fill = self.fill_color, tags = 'preview')
		elif self.tool == 'ellipse':
			self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline = self.stroke_color, fill = self.fill_color, tags = 'preview')

	def on_button_release(self, event):
		self.canvas.delete('preview')
		if self.tool == 'straight_line':
			self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill = self.stroke_color)
		elif self.tool == 'rectangle':
			self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline = self.stroke_color, fill = self.fill_color)
		elif self.tool == 'ellipse':
			self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline = self.stroke_color, fill = self.fill_color)
