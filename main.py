from tkinter import *
from tkinter import font as tkFont

class CalcWindow:
    def __init__(self, win):
        #create and place assets
        #main label
        mainLabelFont = tkFont.Font(size=25, weight="bold")
        self.numberLabel = Label(win, text="0", font=mainLabelFont)
        self.numberLabel.place(x=20, y=40)

        #current operator (blank by default, listed as 'a' for testing purposes
        self.operatorLabel = Label(win, text="a")
        self.operatorLabel.place(x=220, y=40)

        #number buttons
        self.buttonNumOne = Button(win, text="1", height=3, width=6)
        self.buttonNumOne.place(x=20, y=100)
        self.buttonNumTwo = Button(win, text="2", height=3, width=6)
        self.buttonNumTwo.place(x=75, y=100)
        self.buttonNumThree = Button(win, text="3", height=3, width=6)
        self.buttonNumThree.place(x=130, y=100)
        self.buttonNumFour = Button(win, text="4", height=3, width=6)
        self.buttonNumFour.place(x=20, y=160)
        self.buttonNumFive = Button(win, text="5", height=3, width=6)
        self.buttonNumFive.place(x=75, y=160)
        self.buttonNumSix = Button(win, text="6", height=3, width=6)
        self.buttonNumSix.place(x=130, y=160)
        self.buttonNumSeven = Button(win, text="7", height=3, width=6)
        self.buttonNumSeven.place(x=20, y=220)
        self.buttonNumEight = Button(win, text="8", height=3, width=6)
        self.buttonNumEight.place(x=75, y=220)
        self.buttonNumNine = Button(win, text="9", height=3, width=6)
        self.buttonNumNine.place(x=130, y=220)

        #operator buttons
        self.buttonPlus = Button(win, text="+", height=3, width = 6)
        self.buttonPlus.place(x=190, y=100)
        self.buttonMinus = Button(win, text="-", height=3, width=6)
        self.buttonMinus.place(x=190, y=160)
        self.buttonDivide = Button(win, text="/", height=3, width=6)
        self.buttonDivide.place(x=190, y=220)
        self.buttonMult = Button(win, text="x", height=3, width=6)
        self.buttonMult.place(x=250, y=100)

        #other buttons
        self.buttonEquals = Button(win, text="=", height=7, width=6)
        self.buttonEquals.place(x=250, y=160)
        self.buttonBackspace = Button(win, text="<-", height=3, width=6)
        self.buttonBackspace.place(x=250, y=40)

        #TODO: add functions to correspond to these buttons
        #TODO: add functionality to change mainLabelFont for each number button press

window=Tk()
mywin = CalcWindow(window)
window.title("Calculator")
window.geometry("320x300+10+10")
window.mainloop()