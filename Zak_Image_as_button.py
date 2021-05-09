from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk



def set():
    print("Hello World")


root = Tk()
root.geometry("200x150")
imge=ImageTk.PhotoImage(Image.open("capital_anime/asta.jpg"))
frame = Frame(root)
frame.pack()
button = Button(frame, text="Button1",relief=RIDGE,image=imge, command=set,activebackground="blue",activeforeground="orange",justify=RIGHT,width=30,state=NORMAL,pady=20,padx=10,bg="grey",fg="brown",font="Helvetica 20 bold")
button.pack(pady=20)

root.mainloop()