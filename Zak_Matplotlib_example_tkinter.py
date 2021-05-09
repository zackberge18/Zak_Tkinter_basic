import matplotlib.pyplot as plt
from tkinter import *
import numpy as np

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        my_button=Button(text="Graph it",command=self.graph)
        my_button.pack()


    def graph(self):
        house=np.random.normal(200000,25000,5000)
        plt.polar(house)
        plt.show()


if __name__ == '__main__':
    app=App()
    app.mainloop()