# "Typing Speed Test"

import tkinter as tk
import tkinter.font as tkFont


def key_press(event):
    print("pressed", repr(event.char))


def mouse_click(event):
    # frame.focus_set()
    print("clicked at", event.x, event.y)


text = "This is a sentence."
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

root = tk.Tk()
root.title("Typing Speed Test")
root.config(cnf=root_defaults, width=1100, height=600)
root.bind("<Key>", key_press)
root.bind("<Button-1>", mouse_click)
root.focus()

frame = tk.Frame(root, cnf=frame_defaults, width=1000, height=500)
# frame.bind("<Key>", key_press)
# frame.bind("<Button-1>", mouse_click)
frame.pack()
# frame.focus()

canvas = tk.Canvas(frame, cnf=canvas_defaults, relief=tk.SUNKEN, width=800, height=400)
canvas.pack()

text_canvas = canvas.create_text(400, 100, text=text, font=font, justify='left', activefill='white')


root.mainloop()
