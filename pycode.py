from tkinter import *
from tkinter import messagebox

import sys
from userInterface import *


def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    img = PhotoImage(file="lenna.gif")
    x = Display(master, img)
    master.mainloop()


def exit1():
    again=messagebox.askyesno("QUIT","DO YOU REALLY WANT TO QUIT?")
    if(again==True):
        sys.exit()
def showhelp():
    messagebox.showinfo("HELP", "RULES FOR THE GAME:\n1. First to 30th square wins\n2. Special squares have special powers. Either you get hold of a ladder or get bitten by a snake\n3. To gain access to a ladder, a question must be answered. Right answer leads to promotion and wrong answer results in no update in position\n4. If bitten by a snake, you will be demoted to a certain position")
def aboutus():
    messagebox.showinfo("ABOUT US","This game has been developed as a part of our curriculum as IT students.\nThe game has been developed using python version 3.7.2 and above.\nThe game is entirely user interactive.\nThe developers of the game are:\n SHREYA SAKPAL\n HITANSHU SHAH\n PRAVIN ANILKUMAR")

def start():
    main()
root=Tk()
root.geometry("960x650+383+134")
s=PhotoImage(file="sn.png")
l1=Label(root,image=s,anchor="center")
l1.pack()
b1=Button(root,text="START",font=('Comic Sans MS',18),fg="white",bg="red",command=main)
b1.place(x=460,y=250,anchor="center")
b2=Button(root,text="HELP",font=('Comic Sans MS',18),fg="white",bg="red",command=showhelp)
b2.place(x=460,y=350,anchor="center")
b3=Button(root,text="QUIT",font=('Comic Sans MS',18),fg="white",bg="red",command=exit1)
b3.place(x=460,y=450,anchor="center")
b4=Button(root,text="ABOUT US",font=('Comic Sans MS',13),fg="black",command=aboutus)
b4.place(x=840,y=600)
root.mainloop()




