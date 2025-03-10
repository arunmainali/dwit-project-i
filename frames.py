import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class ToolbarFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas_frame = None
        self.stroke_width = tk.DoubleVar(value=2)
        self.stroke_color = tk.StringVar(value = 'black')
        self.color_options = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'white']

        self.load_images()
        self.create_widgets()
        self.create_layout()

    def set_canvas_frame(self, canvas_frame):
        self.canvas_frame = canvas_frame
        self.update_button_commands()

    def load_images(self):
        self.paint_brush_image = ctk.CTkImage(Image.open('images/paint-brush.png'))
        self.eraser_image = ctk.CTkImage(Image.open('images/eraser.png'))
        self.rectangle_image = ctk.CTkImage(Image.open('images/rectangle.png'))
        self.ellipse_image = ctk.CTkImage(Image.open('images/ellipse.png'))
        self.curve_line_image = ctk.CTkImage(Image.open('images/curve-line.png'))
        self.straight_line_image = ctk.CTkImage(Image.open('images/straight-line.png'))

    def create_widgets(self):
        self.paint_brush_button = ctk.CTkButton(self, image=self.paint_brush_image, text='')
        self.eraser_button = ctk.CTkButton(self, image=self.eraser_image, text='')
        self.rectangle_button = ctk.CTkButton(self, image=self.rectangle_image, text='')
        self.ellipse_button = ctk.CTkButton(self, image=self.ellipse_image, text='')
        self.curve_line_button = ctk.CTkButton(self, image=self.curve_line_image, text='')
        self.straight_line_button = ctk.CTkButton(self, image=self.straight_line_image, text='')

        self.stroke_size_slider = ctk.CTkSlider(self, from_=1, to=20, variable=self.stroke_width)

        self.text_button = ctk.CTkButton(self, text='Text', width = 40, height = 40)

        self.stroke_size_slider.grid(row=3, column=0, columnspan=2)
        self.color_label = ctk.CTkLabel(self, text='Color:')
        self.color_dropdown = ctk.CTkOptionMenu(
            self,
            values = self.color_options,
            variable = self.stroke_color,
        )


    def update_button_commands(self):
        self.paint_brush_button.configure(command=self.canvas_frame.select_paint_brush)
        self.eraser_button.configure(command=self.canvas_frame.select_eraser)
        self.rectangle_button.configure(command=self.canvas_frame.select_rectangle)
        self.ellipse_button.configure(command=self.canvas_frame.select_ellipse)
        self.curve_line_button.configure(command=self.canvas_frame.select_curve_line)
        self.straight_line_button.configure(command=self.canvas_frame.select_straight_line)
        self.text_button.configure(command = self.canvas_frame.select_text)

        self.color_dropdown.configure(command=self.on_color_change)
    
    def on_color_change(self, color):
        if self.canvas_frame:
            self.canvas_frame.update_stroke_color(color)

    def create_layout(self):
        # create the grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # place the widgets
        self.paint_brush_button.grid(row=0, column=0)
        self.eraser_button.grid(row=0, column=1)
        self.rectangle_button.grid(row=1, column=0)
        self.ellipse_button.grid(row=1, column=1)
        self.curve_line_button.grid(row=2, column=0)
        self.straight_line_button.grid(row=2, column=1)
        self.text_button.grid(row = 3, column = 0)

        self.color_label.grid(row = 4, column = 0)
        self.color_dropdown.grid(row = 4, column = 1)


class CanvasFrame(tk.Frame):
    def __init__(self, parent, toolbar_frame):
        super().__init__(parent)

        self.toolbar_frame = toolbar_frame

        self.tool = 'paint_brush'
        self.stroke_color = 'black'
        self.fill_color = 'white'
        self.canvas_bg = 'white'

        self.start_x = None
        self.start_y = None

        self.text_widgets = []
        self.active_text = None

        self.create_widgets()
        self.create_layout()

        self.canvas.bind('<Button-1>', self.on_button_press)
        self.canvas.bind('<Button1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg=self.canvas_bg)

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas.grid(row=0, column=0, sticky='nsew')

    def select_paint_brush(self):
        self.tool = 'paint_brush'

    def select_eraser(self):
        self.tool = 'eraser'

    def select_text(self):
        self.tool = 'text'

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

    def update_stroke_color(self, color):
        self.stroke_color = color

    def create_text_box(self, x, y):
        # Create a text entry widget on the canvas
        text_widget = tk.Text(self.canvas, width=20, height=4, wrap=tk.WORD, 
                            font=('Arial', int(self.toolbar_frame.stroke_width.get())), 
                            fg=self.stroke_color)
        
        # Place the text widget at the clicked position
        text_widget_window = self.canvas.create_window(x, y, window=text_widget, anchor=tk.NW)
        
        # Add event handlers for the text widget
        text_widget.bind("<FocusOut>", lambda e, w=text_widget, win=text_widget_window: self.finalize_text(w, win))
        text_widget.bind("<Return>", lambda e, w=text_widget, win=text_widget_window: self.finalize_text(w, win))
        
        # Store and focus the new text widget
        self.text_widgets.append((text_widget, text_widget_window))
        self.active_text = text_widget
        text_widget.focus_set()

    def finalize_text(self, text_widget, window_id):
        # Convert entry widget to permanent text on the canvas
        text_content = text_widget.get("1.0", tk.END).strip()
        
        if text_content:
            # Get the coordinates of the text widget
            x, y = self.canvas.coords(window_id)
            
            # Create permanent text on the canvas
            self.canvas.create_text(
                x, y, 
                text=text_content, 
                font=('Arial', int(self.toolbar_frame.stroke_width.get())),
                fill=self.stroke_color,
                anchor=tk.NW
            )
        
        # Remove the text entry widget
        self.canvas.delete(window_id)
        if (text_widget, window_id) in self.text_widgets:
            self.text_widgets.remove((text_widget, window_id))
        
        self.active_text = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.tool == 'text':
            self.create_text_box(event.x, event.y)

    def on_mouse_drag(self, event):
        self.canvas.delete('preview')
        stroke_width = self.toolbar_frame.stroke_width.get()
        if self.tool == 'paint_brush':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.stroke_color, width = stroke_width, capstyle=tk.ROUND, smooth=True)
            self.start_x, self.start_y = event.x, event.y
        elif self.tool == 'eraser':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.canvas['bg'], width = stroke_width, capstyle=tk.ROUND, smooth=True)
            self.start_x, self.start_y = event.x, event.y
        elif self.tool == 'straight_line':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.stroke_color, width = stroke_width, tags='preview')
        elif self.tool == 'rectangle':
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.stroke_color, fill=self.fill_color, width = stroke_width, tags='preview')
        elif self.tool == 'ellipse':
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.stroke_color, fill=self.fill_color, width = stroke_width, tags='preview')

    def on_button_release(self, event):
        self.canvas.delete('preview')
        stroke_width = self.toolbar_frame.stroke_width.get()
        if self.tool == 'straight_line':
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.stroke_color, width = stroke_width)
        elif self.tool == 'rectangle':
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.stroke_color, fill=self.fill_color, width = stroke_width)
        elif self.tool == 'ellipse':
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.stroke_color, fill=self.fill_color, width = stroke_width)