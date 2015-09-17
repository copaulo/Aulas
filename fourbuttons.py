\\ This program is a lesson of how to use tkinter and creates four buttons using different methods

from tkinter import *
class MyApp:
    def __init__(self, myParent):
        self.container1 = Frame(root)
        self.container1.pack()
        
        self.button1 = Button(self.container1)
        self.button1["text"] = "Aqui tem um bando!"   
        self.button1["bg"] = "white"
        self.button1.pack(side=LEFT)

        self.button2 = Button(self.container1, text='de loucos', bg='tan')
        self.button2.pack(side=LEFT)

        self.button3 = Button(self.container1)
        self.button3.configure(text='Louco por ti')
        self.button3.configure(background = "gray")
        self.button3.pack(side=LEFT)

        self.button4 = Button(self.container1, text='Corinthians!', bg='red')
        self.button4.pack(side=LEFT)

root = Tk()
myapp = MyApp(root)
root.mainloop()
