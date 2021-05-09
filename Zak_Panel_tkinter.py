from tkinter import *

class App(Tk):

    def __init__(self):
        super(App, self).__init__()
        panel_1=PanedWindow(bd=4,relief=SUNKEN,bg="blue",width=40,height=40)

        panel_1.pack(fill=BOTH,expand=1)
        left_label=Label(panel_1,text="for panel_1")
        panel_1.add(left_label)

        panel_2=PanedWindow(panel_1,orient=HORIZONTAL,bd=4,relief="raised")

        panel_1.add(panel_2)
        my=Label(panel_2,text="for panel 2",bd=4,relief="raised")
        panel_2.add(my)
        mine = Label(panel_2, text="for panel 2 label 2",bd=4,relief="raised")
        panel_2.add(mine)


if __name__ == '__main__':
    app=App()
    app.geometry("500x300")
    app.mainloop()

