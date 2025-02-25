import tkinter as tk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill = 'red')

# event binding to create a basic paint app
brush_size = 2
def draw_on_canvas(event):
	x = event.x
	y = event.y
	canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

def brush_size_adjust(event):
	global brush_size
	if event.delta > 0:
		brush_size += 4
	else:
		brush_size -= 4

	brush_size = max(0, min(brush_size, 50))

canvas.bind('<B1-Motion>', draw_on_canvas())
canvas.bind('MouseWheel', brush_size_adjust)

# run
window.mainloop()
