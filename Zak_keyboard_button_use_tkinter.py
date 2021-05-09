


######keyboard Button use

from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title('Binding')
        self.my_btn=Button(text="click me")
        #self.my_btn.grid(row=0,column=0,columnspan=2)
        self.my_btn.pack()
        self.my_btn.bind("<Key>",self.clicker)

    def clicker(self,event):
        self.my_label=Label(text="you clicked"+str(event.char))
        #self.my_label.grid(row=1,column=0)
        self.my_label.pack()

app=App()

app.mainloop()


