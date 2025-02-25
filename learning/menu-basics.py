import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Menus')

# menu
menu = tk.Menu(master = window)
window.configure(menu = menu)

# sub menu
file_menu = tk.Menu(master = menu, tearoff = 0)
file_menu.add_command(label = 'New', command = lambda: print('New File'))
file_menu.add_command(label = 'Open', command = lambda: print('Open'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)

# another submenu
help_menu = tk.Menu(master = menu, tearoff = 0)
help_menu.add_command(label = 'About', command = lambda: print('About'))
help_menu.add_command(label = 'Help Entry', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'Check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = help_menu)

# menu button
menu_button = ttk.Menubutton(master = window, text = 'Menu Button')
menu_button.pack(side = tk.LEFT)

# run
window.mainloop()
