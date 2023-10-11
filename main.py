from tkinter import *
from tkinter import font

class CalcWindow:
    currentOperator = ""
    firstNum = 0.0
    secondNum = 0.0

    #Since default values are 0, need this variable to determine if user wants 0 as an argument
    operatorUsed = False

    def __init__(self, win):
        #create and place assets
        #main label
        mainLabelFont = font.Font(size=25, weight="bold")
        self.numberLabel = Label(win, text="0", font=mainLabelFont)
        self.numberLabel.place(x=20, y=40)

        #current operator (should be blank by default, listed as 'a' for testing purposes
        self.operatorLabel = Label(win, text=self.currentOperator)
        self.operatorLabel.place(x=220, y=40)

        #number buttons
        self.buttonNumOne = Button(win, text="1", height=3, width=6,
                                   command=lambda: self.numberButton("1"))
        self.buttonNumOne.place(x=20, y=100)

        self.buttonNumTwo = Button(win, text="2", height=3, width=6,
                                   command=lambda: self.numberButton("2"))
        self.buttonNumTwo.place(x=75, y=100)

        self.buttonNumThree = Button(win, text="3", height=3, width=6,
                                   command=lambda: self.numberButton("3"))
        self.buttonNumThree.place(x=130, y=100)

        self.buttonNumFour = Button(win, text="4", height=3, width=6,
                                   command=lambda: self.numberButton("4"))
        self.buttonNumFour.place(x=20, y=160)

        self.buttonNumFive = Button(win, text="5", height=3, width=6,
                                   command=lambda: self.numberButton("5"))
        self.buttonNumFive.place(x=75, y=160)

        self.buttonNumSix = Button(win, text="6", height=3, width=6,
                                   command=lambda: self.numberButton("6"))
        self.buttonNumSix.place(x=130, y=160)

        self.buttonNumSeven = Button(win, text="7", height=3, width=6,
                                   command=lambda: self.numberButton("7"))
        self.buttonNumSeven.place(x=20, y=220)

        self.buttonNumEight = Button(win, text="8", height=3, width=6,
                                   command=lambda: self.numberButton("8"))
        self.buttonNumEight.place(x=75, y=220)

        self.buttonNumNine = Button(win, text="9", height=3, width=6,
                                   command=lambda: self.numberButton("9"))
        self.buttonNumNine.place(x=130, y=220)

        self.buttonNumNine = Button(win, text="0", height=3, width=6,
                                    command=lambda: self.numberButton("0"))
        self.buttonNumNine.place(x=20, y=280)

        self.buttonNumNine = Button(win, text=".", height=3, width=6,
                                    command=lambda: self.numberButton("."))
        self.buttonNumNine.place(x=75, y=280)

        #operator buttons
        self.buttonPlus = Button(win, text="+", height=3, width = 6,
                                 command=lambda: self.changeOperator("+"))
        self.buttonPlus.place(x=190, y=100)

        self.buttonMinus = Button(win, text="-", height=3, width=6,
                                  command=lambda: self.changeOperator("-"))
        self.buttonMinus.place(x=190, y=160)

        self.buttonDivide = Button(win, text="/", height=3, width=6,
                                   command=lambda: self.changeOperator("/"))
        self.buttonDivide.place(x=190, y=220)

        self.buttonMult = Button(win, text="x", height=3, width=6,
                                    command=lambda: self.changeOperator("x"))
        self.buttonMult.place(x=250, y=100)

        #other buttons
        #resolve operation button
        self.buttonEquals = Button(win, text="=", height=7, width=6,
                                   command=lambda: self.resolveOperation())
        self.buttonEquals.place(x=250, y=160)

        #backspace button
        self.buttonBackspace = Button(win, text="<-", height=3, width=6,
                                      command=lambda: self.backspace())
        self.buttonBackspace.place(x=250, y=40)

    def backspace(self):
        if not self.operatorUsed:
            if len(self.numberLabel.cget("text")) == 1:
                self.numberLabel.config(text="0")
            else:
                self.numberLabel.config(text=(self.numberLabel.cget("text")[:-1]))
    def changeOperator(self, operatorType):
        self.resolveOperation()
        self.operatorUsed = True
        #change operator labels
        self.currentOperator = operatorType
        self.operatorLabel.config(text=self.currentOperator)

        self.firstNum = float(self.numberLabel.cget("text"))
        print("first number set to " + str(self.firstNum) + " with operator " + operatorType)

        #TODO: handle cases with long numbers
    def resolveOperation(self):
        self.secondNum = float(self.numberLabel.cget("text"))
        match self.currentOperator:
            case "+":
                self.secondNum = float(self.numberLabel.cget("text"))
                self.numberLabel.config(text=str(self.firstNum+self.secondNum))
                self.firstNum = self.firstNum+self.secondNum
            case "-":
                self.secondNum = float(self.numberLabel.cget("text"))
                self.numberLabel.config(text=str(self.firstNum-self.secondNum))
                self.firstNum = self.firstNum-self.secondNum
            case "/":
                self.secondNum = float(self.numberLabel.cget("text"))
                if self.secondNum == 0:
                    self.numberLabel.config(text="Error: divide by 0")
                else:
                    self.numberLabel.config(text=str(self.firstNum/self.secondNum))
                    self.firstNum = self.firstNum/self.secondNum
            case "x":
                self.secondNum = float(self.numberLabel.cget("text"))
                self.numberLabel.config(text=str(self.firstNum*self.secondNum))
                self.firstNum = self.firstNum*self.secondNum
            case _:
                print("idk broski")

        self.operatorUsed = False
    def numberButton(self, button_number: str):
        #Updating numberLabel text
        #Case 1: numberLabel text is shorter than current arbitrary limit and operator wasnt pressed
        if      (not self.operatorUsed and
                (len(self.numberLabel.cget("text")) < 8 and
                self.numberLabel.cget("text") != "0")):
            self.numberLabel.config(text=(self.numberLabel.cget("text")+button_number))

        #Case 2: numberLabel text is shorter than current limit and oprerator WAS pressed
        elif self.operatorUsed:
            #replace numberLabel with new number
            self.numberLabel.config(text=(button_number))

        #TODO: check if this case needs operatorPressed logic added in
        #Case 3: numberLabel text is exactly "0"
        if self.numberLabel.cget("text") == "0":
            if button_number == "0":
                self.numberLabel.config(text="0")
            else:
                self.numberLabel.config(text=button_number)

        #Reset the variable as a new number is being entered
        self.operatorUsed = False

window=Tk()
mywin = CalcWindow(window)
window.title("Calculator - 8 digit limit")
window.geometry("320x350+10+10")
window.mainloop()