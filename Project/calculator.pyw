# CMPT 120 Intro to Programming
# Project #2 – Calculator Graphics
# Created: 2019-12-7

from graphics import*
from calc_functions import calculate


#Creating a class for buttons

class DrawKepads:
    def __init__(self, win):
        self.win= win
        self.buttons = [[16,260,20,80,"","light cyan"], [20,60,100,140,"7","dark blue"],[20,60,150,190,"4","dark blue"],[20,60,200,240,"1","dark blue"],
               [20,60,250,290,'+/-',"orange"], [70,110,100,140,"8","dark blue"],[70,110,150,190,"5","dark blue"],[70,110,200,240,"2","dark blue"],
               [70,110,250,290,"0","dark blue"],[120,160,100,140,"9","dark blue"],[120,160,150,190,"6","dark blue"],[120,160,200,240, "3","dark blue"],
               [120,160,250,290,'.',"orange"], [170,210,100,140," + ","orange"],[170,210,150,190," - ","orange"],[170,210,200,240," * ","orange"],
               [170,210,250,290," / ","orange"], [220,260,100,140,'M+',"gray"],[220,260,150,190,'M-',"gray"],[220,260,200,240,'MR',"gray"],[220,260,250,290,'MC',"gray"],
               [170,210,300,340,'Del',"dark orange"],[220,260,300,340,'=',"green"], [120,160,300,340,'AC',"red"]
               ]

        #Takes one entity of array from self.buttons array and assign it to drawButton.
        for self.button in self.buttons:
            self.drawButton(self.button)
    #retreiving the label in order to check if a button is pressed      
    def getLabel(self,p):
        self.p= p
        for self.button in self.buttons:
            if self.isButtonPressed(self.button,self.p):
                return self.button[4]
    #checking if a certain button pressed.
    def isButtonPressed(self,button, mouse):
        self.b = button
        self.mouse = mouse
        if ( self.b[0]< self.mouse.getX()< self.b[1] and
         self.b[2] < self.mouse.getY()< self.b[3]):
            return True
        else:
            return False
    # drawing one button at a time 
    def drawButton(self, button):
        self.button=button        

        # Create the rectangle for the button
        self.rect=Rectangle( Point(self.button[0],self.button[2]), Point(self.button[1],self.button[3]))
        self.rect.draw(self.win)
        self.rect.setFill(self.button[5])

        # Drawing texts and all details, which are related to text. 
        self.txt=Text( Point(self.button[0] + 20, self.button[3] - 20 ), self.button[4])
        self.txt.draw(self.win)
        self.txt.setTextColor("white")
        self.txt.setSize(18)
# creating for a class for creating a display  
class Displaying:
    #the function for creating the display setting
    def __init__(self, win):
        self.win= win
        self.output=Text(Point(115,50), "")
        self.output.draw(self.win)
        self.output.setSize(18)
    #displaying the equation frequently
    def displayEquation(self,equation,display):
        self.equation= equation
        self.display= display
        self.display.setText(equation)
        pass

#creanting the main class that contains all the calculation.
class Calculator:
    
    def __init__(self):
        self.win=GraphWin('Calculator',280,360)
        self.win.setBackground("royal blue")


         #calling the function drawKeypad, and display in order to scketch the buttons
        #and create some display
        
        self.draw=DrawKepads(self.win)
        self.dis=Displaying(self.win)
        self.display= self.dis.output
        self.equation=""
        self.memory=0

        while True:
            self.click = self.win.getMouse()
            self.label = self.draw.getLabel(self.click)
        
            if self.label == '=':
                self.equation = self.solveEquation(self.equation)
                label=""

            elif self.label == 'AC':
                self.equation=""

            elif self.label == 'Del':
                self.equation= self.equation[:len(self.equation)-1]
            
            elif self.label == '+/-':
                self.result = float(self.solveEquation(self.equation))*-1
                self.equation=""
                self.equation= self.equation + str(self.result)

            elif self.label == 'M+':
                self.memory = self.memory + float(self.solveEquation(self.equation))

            elif self.label == 'M-':
                self.memory= self.memory - float(self.solveEquation(self.equation))

            elif self.label == 'MR':
                self.equation= self.equation + str (self.memory)

            elif self.label == 'MC':
                self.memory=0
            else: 
                self.after = self.buildEquation(self.equation, self.label)
                self.equation= "" 
                self.equation= self.equation + self.after
            self.dis.displayEquation(self.equation,self.display)

    #the method for calculating 
    def solveEquation(self,equation):
        self.equation= equation
        self.final=calculate(self.equation)
        self.equation= ""
        self.equation= self.equation + str(self.final)
        return self.equation

    #the method for building up the equation
    def buildEquation(self, equation,label):
        self.equation= equation
        self.label=label
        self.equation= self.equation + self.label
        return self.equation
    
#the main function to call the calculator.
def main():
    
    calculator= Calculator()
    
main()
