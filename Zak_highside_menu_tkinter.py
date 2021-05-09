from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('500x500')
def for_1():
    messagebox.showinfo("order","1 order placed")
def for_2():
    messagebox.showinfo("order","2 order placed")
def nachos():
    munchies.forget()
    my_label=Label(root,text="How many")
    my_label.pack()
    for_1_button = Button(root, text="1", height=5, width=20, command=for_1)
    for_1_button.pack()
    for_2_button = Button(root, text="2", height=5, width=20, command=for_2)
    for_2_button.pack()
def smoked_salmon():
    messagebox.showinfo("order","your order for smoked salmon has been placed")
    root.destroy()
def chicken():
        messagebox.showinfo("order", "your order for chicken has been placed")
        root.destroy()
def munchies_app():
    global munchies
    munchies=Frame(root)
    munchies.pack()
    nachos_button=Button(munchies,text="nachos",height=5,width=20,command=nachos)
    nachos_button.pack()
    smoked_salmon_button = Button(munchies, text="smoked salmon", height=5, width=20,command=smoked_salmon)
    smoked_salmon_button.pack()
    chicken_button = Button(munchies, text="chicken", height=5, width=20,command=chicken)
    chicken_button.pack()
    munchies_button.destroy()

def back_btn():
    pass

def forward_btn():
    pass


munchies_button=Button(root,text="Munchies",command=munchies_app,height=5,width=20)
munchies_button.pack()
munchies_button.place(x=0,y=0)
back_button=Button(root,text='<<',command=back_btn,relief=RAISED)
forward_button=Button(root,text='>>',command=forward_btn,relief=RAISED)
back_button.pack(anchor=NE)
back_button.place(y=200)
forward_button.pack(anchor=NW)
forward_button.place(y=100)
root.mainloop()