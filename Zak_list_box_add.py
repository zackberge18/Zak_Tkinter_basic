

#########ADd List BOx
from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("400x400")
        self.config(bg='SlateGray3')
        self.title("addressbook")

        self.contactlist=[
            ['zack','1231233'],
            ['ukena','2567446'],
            ['edi','5465477']
        ]
        self.Name=StringVar()
        self.Number=StringVar()
        self.frame=Frame(self)
        self.frame.pack(side=RIGHT)

        self.scroll=Scrollbar(self.frame,orient=VERTICAL)
        self.select=Listbox(self.frame,yscrollcommand=self.scroll.set,height=12)
        for i in range(len(self.contactlist)):
            self.select.insert(i,self.contactlist[i])

        self.scroll.config(command=self.select.yview)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.select.pack(side=LEFT,fill=BOTH,expand=1)

        self.e_name=Entry(self)
        self.e_name.place(x=100,y=20)
        self.e_number=Entry(self)
        self.e_number.place(x=100, y=40)

        Button(text="ADD",command=self.AddContact).place(x=50,y=110)
        Button(text="selected", command=self.Selected).place(x=50, y=200)

    def Selected(self):
        print(self.select.curselection()[0])
        return int(self.select.curselection()[0])
    def AddContact(self):
        self.select.insert(END,self.e_name.get()+self.e_number.get())




if __name__ == '__main__':

    app=App()
    app.mainloop()
