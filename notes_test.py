from tkinter import *
from tkinter.filedialog import asksaveasfilename

root = Tk()
root.geometry("350x250")
root.title("Test")
root.minsize(height=250, width=350)
root.maxsize(height=1080, width=1080)

# adding scrollbar
scrollbar = Scrollbar(root)

# packing scrollbar
scrollbar.pack(side=RIGHT,fill=Y)

text_info = Text(root,yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

root.mainloop()
