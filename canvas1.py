# see these YouTube videos:
# https://www.youtube.com/watch?v=7MiBgdZXRz4&index=29&list=PLbW_am_GRTo1J1iKtLjSORkzLioT05u-I

from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)
line = canvas.create_line(0,0, 100, 100, fill='blue', width=5)
canvas.itemconfigure(line, fill='green')
canvas.coords(line)
canvas.coords(line, 0, 0, 100, 100, 200, 0, 300, 100, 400, 0)
root.mainloop()
