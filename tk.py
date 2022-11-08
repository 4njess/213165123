from random import randint
import time
from tkinter import DISABLED, Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Frame, Button, Style
import tkinter.font as font
 
b = randint(0,100)
c = randint(0,100)

d = b + c

a1 = 0
a2 = 0

q = randint(1,2)
if q == 1:
    a1 = d
    a2 = randint(0,100)
else:
    a2 = d
    a1 = randint(0,100)  



a = ['-','+']
class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Математический тест")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        Style().configure("TFrame", background="#c5dfe4")





        Button0 = tk.Button(self, text=f'{b}  +  {c}  =  ? ', height=4, width=16, background="#c5dfe4", font=24, border=0)
        Button0.place(x=250, y=100)

        Button1 = tk.Button(self, text=a1, height=2, width=12, background="#8bbdcf", font=24, border=0.5,command=self.a1_b)
        Button1.place(x=125, y=375)

        Button2 = tk.Button(self, text=a2, height=2, width=12, background="#8bbdcf", font=24, border=0.5, command=self.a2_b)
        Button2.place(x=375, y=375)
    def a1_b(self):
        if a1 == d:          
            Button1 = tk.Button(self, text=a1, height=2, width=12, background="green", font=24, border=0.5,command=self.a1_b)
            Button1.place(x=125, y=375)
            Style().configure("TFrame", background="#b3f7b3")
            Button0 = tk.Button(self, text=f'{b}  +  {c}  =  ? ', height=4, width=16, background="#b3f7b3", font=24, border=0)
            Button0.place(x=250, y=100)
            Button0.place(x=250, y=100)
        else:
            Button1 = tk.Button(self, text=a1, height=2, width=12, background="red", font=24, border=0.5,command=self.a1_b)
            Button1.place(x=125, y=375)
            
    def a2_b(self):
        if a2 == d:
            Button2 = tk.Button(self, text=a2, height=2, width=12, background="green", font=24, border=0.5,command=self.a1_b)
            Button2.place(x=375, y=375)
            Style().configure("TFrame", background="#b3f7b3")
            Button0 = tk.Button(self, text=f'{b}  +  {c}  =  ? ', height=4, width=16, background="#b3f7b3", font=24, border=0)
            Button0.place(x=250, y=100)
        else:
            Button2 = tk.Button(self, text=a2, height=2, width=12, background="red", font=24, border=0.5,command=self.a1_b)
            Button2.place(x=375, y=375)
            
 
def main():
    root = Tk()
    root.geometry("600x600+300+300")
    Example(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

 
