from tkinter import *
from tkinter import colorchooser

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.my_button=Button(text="pick a color",command=self.color)
        self.my_button.pack()
    def color(self):
        self.my_color=colorchooser.askcolor()
        the_label=Label(text=self.my_color[1],bd=5)
        the_label.pack()
        the_label = Label(text="THE COLOR YOU CHOOSE IS BG", bd=5,bg=self.my_color[1])
        the_label.pack()
        print(self.my_color)




if __name__ == '__main__':
    app=App()
    app.mainloop()