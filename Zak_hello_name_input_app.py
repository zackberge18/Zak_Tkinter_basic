###### tKINTER hello nAME INPUT aPP
from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.e=Entry(width=50,font=("arial",35))
        self.e.grid(row=0,column=0,padx=10,pady=10)
        self.mybutton=Button(text="Enter YOur Name",command=self.my_click)
        self.mybutton.grid(row=1,column=0,pady=10)
      # delete_button = Button(text="delete", command=self.delete)
      # delete_button.grid(row=2,column=0,pady=10)
    def my_click(self):
        hello="hello  "+self.e.get()
        self.mylabel=Label(text=hello,font=("arial",35))
        self.mylabel.grid(row=3,column=0,padx=10,pady=10)
        self.e.delete(0,END)
        #self.mybutton['state']=DISABLED
    #def delete(self):
       #if self.mylabel.winfo_exists()==1:
       #    self.mylabel.destroy()
       #self.mybutton['state'] = NORMAL
       #print(self.mybutton.winfo_exists())


if __name__ == '__main__':
    app=App()
    app.mainloop()
