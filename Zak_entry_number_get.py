import tkinter as tk
from pytube import YouTube
import base64


"""class App(tk.Tk):
    def __init__(self):
        super().__init__()
        Label(text="fuck you").pack()


if __name__  ==  "__main__":
    app = App()
    app.mainloop()

"""
root=tk.Tk()
zero=0
def ppp():


    global zero
    a=int(entry_box.get())
    zero+=a

    b = tk.Label(root, text=f"{zero}")
    b.pack()





tk.Label(root,text="enter your name").pack()
entry_box=tk.Entry(root,width=30)
entry_box.pack()

tk.Button(root,text="click me",command=lambda :ppp()).pack()

b = tk.Label(root, text=f"{zero}")
b.pack()



root.mainloop()
