from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Test")
root.minsize(height=250, width=350)
root.maxsize(height=1080, width=1080)

variable = StringVar(root)
variable.set("one") # default value

w = OptionMenu(root, variable, "one", "two", "three")
w.pack()

root.mainloop()
