from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.my_menu=Menu()
        self.config(menu=self.my_menu)
        self.geometry("500x500")

        #create a menu system
        self.file_menu=Menu(self.my_menu)
        self.my_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New..",command=self.file_new)

        #cretate a menu item
        self.edit = Menu(self.my_menu)
        self.my_menu.add_cascade(label="me", menu=self.edit)
        self.edit.add_command(label="you..", command=self.edit_new)


    def your_command(self):
        Label(text="i love u").pack()
    def our_command(self):
        Label(text="i hate u").pack()

    def file_new(self):

        # create some frames
        #self.hide_aall_frames()
        self.file_new_frame = Frame(self, width=400, height=400, bg="red", bd=4)
        self.file_new_frame.pack(fill="both",expand=1)
        the_label = Label(self.file_new_frame,text="THE COLOR YOU CHOOSE IS BG", bd=5, bg="orange")
        the_label.pack()





    def edit_new(self):
        # create some frames
        #self.hide_aall_frames()
        self.editas = Frame(self, width=400, height=400, bg="blue", bd=4)
        self.editas.pack(fill="both", expand=1)
        the_label = Label(self.editas,text="THE COLOR YOU CHOOSE IS BG", bd=5, bg="white")
        the_label.pack()

    def hide_aall_frames(self):
        try:
            self.file_new_frame.pack_forget()
            self.editas.pack_forget()
        except:
            pass
if __name__ == '__main__':
    app=App()
    app.mainloop()
