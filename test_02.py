import tkinter as tk

# colors for certain characters
colormap = {'b':'blue', 'c':'cyan', 'g':'green', 'm':'magenta', 'o':'orange', 'p':'pink', 'r':'red', 'y':'yellow'}


def on_key_press(event):
    if event.char in colormap:
        # attach a tag (the character itself) if the character is in the colormap
        event.widget.tag_add(event.char, 'insert - 1c', 'insert')  # 'end'


def on_key_release(event):
    if event.char in colormap:
        # attach a tag (the character itself) if the character is in the colormap
        event.widget.tag_add(event.char, 'insert - 1c', 'insert')  # 'end'


root = tk.Tk()

text = tk.Text(root, background='#2b2b2b')
text.pack()
text.bind('<KeyPress>', on_key_press)
text.bind('<KeyRelease>', on_key_release)

# setup colors for certain characters using tag_config(...)
for c in colormap:
    text.tag_config(c, background=colormap[c])

root.mainloop()
