# "Typing Speed Test"

import tkinter as tk


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)


text = "This is a sentence."
defaults = {
    'background': '#3c3f41',
    'highlightbackground': '#2b2b2b',
    'highlightcolor': '#4e5254',
    # 'red': '#932019',
    # 'amber': '#a67a19',
    # 'green': '#329a42',
}

root = tk.Tk()
root.title("Typing Speed Test")
root.config(cnf=defaults)

frame = tk.Frame(root, cnf=defaults, width=1000, height=500)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
frame.focus()




root.mainloop()
