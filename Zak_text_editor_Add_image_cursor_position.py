from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.my_text=Text(width=60,height=20,font="arial 10 bold",selectbackground="yellow",selectforeground="black")
        self.my_text.pack()
        global  my_image
        self.my_image=ImageTk.PhotoImage(Image.open("capital_anime/sasuke.jpg"))
        self.open_text=Button(text="grap",command=self.open_file)
        self.open_text.pack()
        self.save_button = Button(text="save", command=self.save)
        self.save_button.pack()
        self.image_button = Button(text="image", command=self.image_add)
        self.image_button.pack()
    def image_add(self):

        self.my_image=ImageTk.PhotoImage(Image.open("capital_anime/sasuke.jpg"))
        position=self.my_text.index(INSERT)
        self.my_text.image_create(position,image=self.my_image)

    def open_file(self):
       text_file=filedialog.askopenfilename(initialdir="C:/",title="text file",filetypes=(("Text Files",'*.txt'),))
       text_file_2=open(text_file,"r")
       stuff=text_file_2.read()
       self.my_text.insert(END,stuff)

       text_file_2.close()
    def save(self):
        text_file=open("sample.txt","w")
        text_file.write(self.my_text.get(1.0,END))

if __name__ == '__main__':
    app=App()
    app.mainloop()