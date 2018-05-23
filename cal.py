from tkinter import *
import math
from tkinter import messagebox
def factorial(n):
        if n==0:
            return 1
        else:
            return n *factorial(n-1)
class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0
        deFont= "Time Roman",12,"italic"
        self.entry = Entry(master, bg="#5BC8AC", bd=5,insertwidth=4,width=25,  font=deFont,  justify=RIGHT,
                           validate="key")
    

        #Number
        self.button1=Button(master,text= "1", command=lambda:self.appendToDisplay("1"))
        self.button2=Button(master,text= "2", command=lambda:self.appendToDisplay("2"))
        self.button3=Button(master,text= "3", command=lambda:self.appendToDisplay("3"))
        self.button4=Button(master,text= "4", command=lambda:self.appendToDisplay("4"))
        self.button5=Button(master,text= "5", command=lambda:self.appendToDisplay("5"))
        self.button6=Button(master,text= "6", command=lambda:self.appendToDisplay("6"))
        self.button7=Button(master,text= "7", command=lambda:self.appendToDisplay("7"))
        self.button8=Button(master,text= "8", command=lambda:self.appendToDisplay("8"))
        self.button9=Button(master,text= "9", command=lambda:self.appendToDisplay("9"))
        self.button0=Button(master,text= "0", command=lambda:self.appendToDisplay("0"))
        self.buttondot=Button(master,text= ".", command=lambda:self.appendToDisplay("."))
        
        self.add_button = Button(master, text="+", command=lambda: self.appendToDisplay("+"))
        self.subtract_button = Button(master, text="-", command=lambda: self.appendToDisplay("-"))
        self.multiply_button=Button(master,text= "*", command= lambda:self.appendToDisplay("*"))
        self.division_button=Button(master,text = "/",command=lambda:self.appendToDisplay("/"))
        self.percentage_button=Button(master,text= "%",command=lambda:self.appendToDisplay("%"))
        self.sin_button=Button(master,text= "Sin", command=lambda:self.appendSin())
        self.cos_button=Button(master,text= "Cos", command=lambda:self.appendCos())
        self.tan_button=Button(master,text= "Tan", command=lambda:self.appendTan())
        self.sqrtRoot_Button=Button(master,text="√",command=lambda:self.appendSqrtRoot())
        self.sqrt_Button=Button(master,text= "x²",command=lambda:self.appendSqrt())
        self.threeSqrt_Button=Button(master,text= "x³",command= lambda:self.appendThreeSqrt())
        self.percentButton=Button(master,text= "%",command= lambda:self.appendPercent())
        self.fact_Button=Button(master,text= "!",command= lambda:self.appendFactorial())
        self.xButton=Button(master,text= "1/x",command= lambda:self.appendX())
        self.reset_button = Button(master, text="Clear", command=lambda: self.appendClear())
        self.equals = Button(master, text = "=",command = lambda:self.calculateExpression())
        self.threeSqrtRoot_Button=Button(master,text= "∛",command= lambda:self.appendThreeSqrtRoot())
        self.logButton=Button(master,text= "logx",command= lambda:self.appendLog())                         
        self.powTenButton=Button(master,text= "10^x",command= lambda:self.appendPow())                                
        self.firstBlacket=Button(master,text="(", command= lambda:self.appendToDisplay("("))
        self.secondBlacket=Button(master,text=")",command=lambda:self.appendToDisplay(")"))
        self.pieButton=Button(master,text= "Ω",command=lambda:self.appendPie())
        self.expButton=Button(master,text= "e",command=lambda:self.appendExp())
        self.expXButton=Button(master,text= "Expx",command=lambda:self.appendExpx())
        self.twoPowerButton=Button(master,text= "2^x",command=lambda:self.appendTwoPower())

        # LAYOUT

        self.entry.grid(row=1, column=0, columnspan=10, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiply_button.grid(row=2,column=2)
        self.division_button.grid(row=2,column=3)
 
        self.equals.grid(row = 6, column = 3, pady = 5)   
        self.button9.grid(row=3,column=0)
        self.button8.grid(row=3,column=1)
        self.button7.grid(row=3,column=2)
        self.button6.grid(row=4,column=0)
        self.button5.grid(row=4,column=1)
        self.button4.grid(row=4,column=2)
        self.button3.grid(row=5,column=0)
        self.button2.grid(row=5,column=1)
        self.button1.grid(row=5,column=2)
        self.button0.grid(row=6,column=0,columnspan=2,sticky=W+E)
        self.buttondot.grid(row=6,column=2)
        
        self.firstBlacket.grid(row=3,column=3)
        self.secondBlacket.grid(row=4,column=3)
        self.xButton.grid(row=5,column=3)
        self.percentButton.grid(row=6,column=4)
 

        self.reset_button.grid(row=2, column=4, columnspan=5,sticky=W+E)
        self.sqrt_Button.grid(row=3,column=4)
        self.threeSqrt_Button.grid(row=4,column=4)
        self.fact_Button.grid(row=5,column=4)
        
        self.sqrtRoot_Button.grid(row=3,column=5)
        self.threeSqrtRoot_Button.grid(row=4,column=5)
        self.powTenButton.grid(row=5,column=5)
        self.twoPowerButton.grid(row=6,column=5)

        self.pieButton.grid(row=3,column=6)
        self.expButton.grid(row=4,column=6)
        self.expXButton.grid(row=5,column=6)
        self.logButton.grid(row=6,column=6)

        self.sin_button.grid(row=3,column=7)
        self.cos_button.grid(row=4,column=7)
        self.tan_button.grid(row=5,column=7)
    def appendX(self):
        self.entryText = self.entry.get()
        texts= 1/eval(self.entryText)
 
        self.textLength = len(self.entryText)
        self.replaceText("")
        self.entry.insert(self.textLength,texts)
   
    def appendPie(self):
        self.entryText = self.entry.get()
        texts= str(math.pi)
 
        self.textLength = len(self.entryText)
        if self.entryText=="0":
            self.replaceText("")
            self.entry.insert(self.textLength,texts)
        
        elif self.entryText=="3.141592653589793":
             self.replaceText("")
             self.entry.insert(self.textLength,texts)
        elif self.entryText!="3.141592653589793":
             self.replaceText("")
             self.entry.insert(self.textLength,texts)
        else:
            self.entry.insert(self.textLength,texts)
    def appendPow(self):
        self.entryText = self.entry.get()
        texts= math.pow(10,eval(self.entryText))
 
        self.textLength = len(self.entryText)
        self.replaceText("")
        self.entry.insert(self.textLength,texts)
    def appendExp(self):
        self.entryText = self.entry.get()
        texts= str(math.e)
 
        self.textLength = len(self.entryText)
        if self.entryText=="0":
            self.replaceText("")
            self.entry.insert(self.textLength,texts)
        
        elif self.entryText=="2.718281828459045":
             self.replaceText("")
             self.entry.insert(self.textLength,texts)
        elif self.entryText!="2.718281828459045":
             self.replaceText("")
             self.entry.insert(self.textLength,texts)
        else:
            self.entry.insert(self.textLength,texts)
    def appendExpx(self):
        self.entryText = self.entry.get()
        self.textLength = len(self.entryText)
        try:
            texts= math.exp(eval(self.entryText))
            self.textLength = len(self.entryText)
            self.replaceText("")
            self.entry.insert(self.textLength,texts)
        except:
            self.replaceText("")
            self.entry.insert(self.textLength, "Its has a math range error")
    def appendTwoPower(self):
        self.entryText = self.entry.get()
        self.textLength = len(self.entryText)
        try:
            texts= pow(2,eval(self.entryText))
            self.textLength = len(self.entryText)
            self.replaceText("")
            self.entry.insert(self.textLength,texts)
        except:
            self.replaceText("")
            self.entry.insert(self.textLength, "Its has a math range error")           
    def replaceText(self, text):
        self.entry.delete(0, END)
        self.entry.insert(0, text)
    def appendToDisplay(self, text):
        self.entryText = self.entry.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        
        else:
            self.entry.insert(self.textLength, text)
    def appendSqrt(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        sqrtNumber= pow(eval(self.entryText),2)
        self.replaceText("")
        self.entry.insert(self.textLength,sqrtNumber)
    def appendThreeSqrt(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        sqrtNumber= pow(eval(self.entryText),3)
        self.replaceText("")
        self.entry.insert(self.textLength,sqrtNumber) 
    def appendSqrtRoot(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        sqrtRootNumber= math.sqrt(eval(self.entryText))
        self.replaceText("")
        self.entry.insert(self.textLength,sqrtRootNumber)
    def appendThreeSqrtRoot(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        sqrtRootNumber= (eval(self.entryText))**(1/3)
        self.replaceText("")
        self.entry.insert(self.textLength,sqrtRootNumber) 
    def appendSin(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)
        sinNumber= format(math.sin(math.radians(eval(self.entryText))), ".9")
        self.replaceText("")
        self.entry.insert(self.textLength,sinNumber) 
    def appendCos(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)
        cosNumber= format(math.cos(math.radians(eval(self.entryText))),".9")
        self.replaceText("")
        self.entry.insert(self.textLength,cosNumber)
    def appendTan(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)
        TanNumber= format(math.tan(math.radians(eval(self.entryText))),".9" )
        self.replaceText("")
        self.entry.insert(self.textLength,TanNumber) 

    def appendClear(self):
        self.replaceText("0")
    
    def appendFactorial(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        factNumber= factorial(eval(self.entryText))
        self.replaceText("")
        self.entry.insert(self.textLength,factNumber)  
    def appendLog(self):
        self.entryText=self.entry.get()
        self.textLength=len(self.entryText)
        logNumber=math.log10(eval(self.entryText))
        self.replaceText("")
        self.entry.insert(self.textLength, logNumber)
    def appendPercent(self):
        self.entryText= self.entry.get()
        self.textLength= len(self.entryText)

        percentNumber= eval(self.entryText)/100
        self.replaceText("")
        self.entry.insert(self.textLength,percentNumber)  
        
    def calculateExpression(self):#python's calculate function 
        self.expression = self.entry.get()
        self.expression = self.expression.replace("%", "/ 100")

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=root)


    
        
root = Tk()
my_gui = Calculator(root)
root.mainloop()
