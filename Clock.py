from tkinter import *
from tkinter.ttk import *

from tkinter.font import Font
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

clock_font = Font(root=root, font="TkFixedFont")
clock_font.configure(size=80)
label = Label(root, font=clock_font, background = "black", foreground = "green")
label.pack(anchor='center')
time()

mainloop()
