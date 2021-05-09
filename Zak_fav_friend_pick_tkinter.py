#### Favororite Friend chooser

from tkinter import *
import random
class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("500x300")

        self.entries=["riley",'ricky','Loren','darel','ME MYSELF AND I']
        toplabel=Label(text="MY favorite",font=("Helvetica",25))
        toplabel.pack(padx=10,pady=20)
        win_button=Button(text="CHOOSE",font=("Helvetica",25),padx=10,pady=10,command=self.pick)
        win_button.pack()
    def pick(self):
        global winner_label
        a=random.choice(self.entries)
        try :
            winner_label.forget()
        except:
            pass

        winner_label=Label(text=a,font=("Helvetica",25),width=30)
        winner_label.pack(pady=20)

if __name__ == '__main__':
    app=App()
    app.mainloop()
