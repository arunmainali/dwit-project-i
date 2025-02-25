import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Customizing Window')
# window.geometry('600x400+left+top')
# window.geometry('600x400+0+0')
# icon
# NOTE: there are websites that convert jpg or png files to an ico file
# window.iconbitmap('file-path.ico')

# exercise
# start the window in the middle of the screen

window_width = 1400
window_height = 800
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# window sizes
window.minsize(200, 100)
# window.maxsize(800, 700)
window.resizable(True, True)

# screen attributes
# very useful
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 0.5)
window.attributes('topmost', True)

# this makes it impossible to close the window
# window.attributes('-disabled', True)
# window.attributes('fullscreen', True)
# security event
window.bind('<Escape>', lambda event: window.quit())

# title bar
# hide the title bar
# when hiding, cannot resize
window.overrideredirect(True)
grip = ttk.Sizegrip(master = window)
# do not pack, only for illustration purposes
# grip.pack()
grip.place(relx = 1.0, rely =  1.0, anchor = 'se')


# run
window.mainloop()
