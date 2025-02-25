import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Testing Canvas')

# canvas
canvas = tk.Canvas(master = window, bg = 'white')
canvas.pack()

brush_size_slider_value = tk.DoubleVar(value = 2)
def draw_on_canvas(event):
	x = event.x
	y = event.y
	brush_size = brush_size_slider_value.get()
	canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

brush_size_slider = ttk.Scale(master = window,
							  from_ = 0, to = 10,
							  orient = 'horizontal',
							  variable = brush_size_slider_value)
brush_size_slider.pack()

canvas.bind('<B1-Motion>', draw_on_canvas)

# run
window.mainloop()
