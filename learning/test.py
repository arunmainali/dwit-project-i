import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Cancas')

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# width is the border width
canvas.create_rectangle((50, 20, 200, 100), fill = 'red', width = 10, dash = (1, 2)) # left, top, right, bottom
# dash(size of the dash, gap between the dashes)

def draw_on_canvas(event):
	x = event.x
	y = event.y
	# canvas.create_oval((left, top, right, bottom))
	canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

def brush_size_adjust(event):
	global brush_size
	# add an if statement
	print(event)

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<Button-1>', brush_size_adjust)

# slider
# scale = ttk.Scale(window,
# 				  command = lambda value: print(value),
# 				  from_ = 0,
# 				  to = 25,
# 				  orient = 'horizontal',
# 				  variable = brush_size,)
# scale.pack()

# run
window.mainloop()
