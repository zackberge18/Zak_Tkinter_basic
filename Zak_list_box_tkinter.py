from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("500x500")
        self.config(bg="black")

        #Create Frame Aand scrollbar
        self.my_frame=Frame(self)
        self.my_frame.pack()
        self.my_scrolbar=Scrollbar(self.my_frame,orient=VERTICAL)
        # LIST BOX wigdet
        ## SINGLE,BRoWSE
        self.my_listbox=Listbox(self.my_frame,width=20,height=20,bg="gray",fg="white",yscrollcommand=self.my_scrolbar.set,selectmode=MULTIPLE)

        self.my_listbox.pack(side=LEFT)
        #confige scroll box
        self.my_scrolbar.config(command=self.my_listbox.yview)
        self.my_scrolbar.pack(side=RIGHT,fill=Y)


        ##Add item to listbox
        self.my_listbox.insert(0,"this is an item")
        self.my_listbox.insert(0, "this is 2 item")
        self.my_listbox.insert(0, "this is 3 item")


        self.my_list=['one','two','three']

        for i in range(20):
            for item in self.my_list:
                self.my_listbox.insert(3,item)

        self.my_button=Button(text="Delete",command=self.delete_func)
        self.my_button.pack()
        self.my_button2 = Button(text="Select", command=self.select)
        self.my_button2.pack()
        self.mylabel=Label(self,text="")
        self.mylabel.pack(pady=10)
        self.my_button2 = Button(text="Deleteall", command=self.delete_all)
        self.my_button2.pack()

    def delete_func(self):
        print(self.my_listbox.get(ANCHOR))

    def delete_all(self):
        self.my_listbox.delete(0,END)
    def select(self):
        self.mylabel.config(text=self.my_listbox.get(ANCHOR))

if __name__ == '__main__':
    app=App()
    app.mainloop()