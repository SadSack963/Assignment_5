# "Typing Speed Test"

import tkinter as tk
import tkinter.font as tkFont
import random_word
from time import sleep


def key_press(event):
    print("pressed", repr(event.char))


def mouse_click(event):
    # frame.focus_set()
    print("clicked at", event.x, event.y)


font = ('Arial', 36, 'bold')

root_defaults = {
    'background': '#000000',
    'highlightbackground': '#1b1b1b',
    'highlightcolor': '#4e5254',
}

frame_defaults = {
    'background': '#3c3f41',
    'highlightbackground': '#2b2b2b',
    'highlightcolor': '#4e5254',
}

canvas_defaults = {
    'background': '#6c6f71',
    'highlightbackground': '#5b5b5b',
    'highlightcolor': '#4e5254',
}

text_defaults = {
    'red': '#932019',
    'amber': '#a67a19',
    'green': '#329a42',
    'white': '#ffffff',
}


text = random_word.get_word(5)
text_length = len(text)

root = tk.Tk()
root.title("Typing Speed Test")
root.config(
    cnf=root_defaults,
    width=1100,
    height=600
)
root.bind("<Key>", key_press)
root.bind("<Button-1>", mouse_click)
root.focus()

frame = tk.Frame(
    root,
    cnf=frame_defaults,
    width=1000,
    height=500
)
# frame.bind("<Key>", key_press)
# frame.bind("<Button-1>", mouse_click)
frame.pack()
# frame.focus()

canvas = tk.Canvas(
    frame,
    cnf=canvas_defaults,
    relief=tk.SUNKEN,
    width=800,
    height=400,
)
canvas.pack()

text_canvas = canvas.create_text(
    1000,
    25,
    text=text,
    font=font,
    anchor="w",
    activefill='white',
    tags=('text',),
)

# Get the space required by the text
(x0, y0, x1, y1) = canvas.bbox('text')
width = x1 - x0
height = y1 - y0
# Set the canvas to accommodate the text
canvas.configure(width=width, height=height)

# if x1 < 0 or y0 < 0:
#     x0 = canvas.winfo_width()
#     y0 = int(canvas.winfo_height() / 2)
#     canvas.coords('text', x0, y0)
    # canvas.move(text_canvas, x0, 0)
for _ in range(text_length * 250):
    canvas.move(text_canvas, -1, 0)
    canvas.update()
    sleep(.01)

# text_widget = tk.Text(
#     master=frame,
#     cnf=canvas_defaults,
#     font=font,
#     wrap=tk.WORD,
#     height=5,
#     width=40,
# )
# text_widget.pack()
# text_widget.insert("1.0", chars=text)


root.mainloop()
