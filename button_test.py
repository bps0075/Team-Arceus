from tkinter import *
from tkinter.filedialog import asksaveasfilename

root = Tk()
root.geometry("350x250")
root.title("Test")
root.minsize(height=250, width=350)
root.maxsize(height=1080, width=1080)

def save():
  filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
  if not filepath:
    return 
    with open(filepath, "w") as output_file:
      text = Editor.get(1.0, tk.END)
      output_file.write(text)
  root.title(f"Entitled - {filepath}")

button = Button(root,text='Save',font=('normal',10),command=save, bg='grey')
button.place(x=0,y=0)

button = Button(root,text='Save',font=('normal',10),command=save, bg='grey')
button.place(x=40,y=0)

root.mainloop()
