import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, geometry):

		# setup
		super().__init__()
		self.title(title)
		self.geometry(f'{geometry[0]}x{geometry[1]}')
		self.minsize(geometry[0], geometry[1])

		# widgets
		self.widget = Menu(self)
		self.main = Main(self)

		# run
		self.mainloop()

class Menu(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

		self.create_widgets()

	def create_widgets(self):

		# create the widgets
		menu_button1 = ttk.Button(self, text = 'Button1')
		menu_button2 = ttk.Button(self, text = 'Button2')
		menu_button3 = ttk.Button(self, text = 'Button3')

		menu_slider1 = ttk.Scale(self, orient = 'vertical')
		menu_slider2 = ttk.Scale(self, orient = 'vertical')

		toggle_frame = ttk.Frame(self)
		menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'Check 1')
		menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'Check 2')

		entry = ttk.Entry(self)

		# create the grid
		self.columnconfigure((0, 1, 2), weight=1, uniform='a')
		self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

		# place the widgets
		menu_button1.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2)
		menu_button2.grid(row = 0, column = 2, sticky = 'nswe')
		menu_button3.grid(row = 1, column = 0, columnspan = 3,sticky = 'nswe')

		menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = 'nswe', pady = 20)
		menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = 'nswe', pady = 20)

		toggle_frame.grid(row = 2, column = 0, columnspan = 3, sticky = 'nswe')
		menu_toggle1.pack(side = 'left', expand = True)
		menu_toggle2.pack(side = 'left', expand = True)

		entry.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')

class Main(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(relx = 0.3, y = 0, relwidth = 0.3, relheight = 1)

		frame = ttk.Frame(self)
		label = ttk.Label(frame, text = 'Test 1', style = 'Red.TLabel')
		button = ttk.Button(frame, text = 'Button')

		label.pack(expand = True, fill = 'both')
		button.pack(expand = True, fill = 'both', pady = 10)

		frame.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)

App('Class based window', (600, 600))
