# CMPT 120 Intro to Programming
# Project #2 – Calculator Graphics
# Created: 2019-10-17

from graphics import*
from calc_functions import calculate

#Takes one entity of array from drawkeypad function and draw using all detailsprovided.
def drawButton(button, win):
    
    x1 = button[0]
    x2 = button[1]
    y1 = button[2]
    y2 = button[3]
    
    label = button[4]
    colorx = button[5]

    # Create the rectangle for the button

    rect=Rectangle( Point(x1,y1), Point(x2,y2))
    rect.draw(win)
    rect.setFill(colorx)

    # Drawing texts and all details, which are related to text. 
    txt=Text( Point(x1 + 20, y2 - 20 ), label)
    txt.draw(win)
    txt.setTextColor("white")
    txt.setSize(18)

# Detecting the mouse click and returning if a button is clicked.
def isButtonPressed(button, mouse):
    x1 = button[0]
    x2 = button[1]
    y1 = button[2]
    y2 = button[3]
    
    if (x1 < mouse.getX()< x2) and (y1 < mouse.getY()< y2):
        return True
    else:
        return False


# This function will helps us take one element of the array and send it to drawbutton in order to get them drawn.
def drawKeypad(buttons,win):
    for button in buttons:
        drawButton(button, win)

def getLabel(buttons, p):
    for button in buttons:
        if isButtonPressed(button,p):
            return button[4]

#the function for creating the display setting
def createdisplay(win):
    output=Text(Point(115,50), "")
    output.draw(win)
    output.setSize(18)
    
    return output

def solveEquation(equation):
    final=calculate(equation)
    equation= ""
    equation= equation + str(final)
    return equation

def buildEquation(equation,label):
    equation= equation + label
    print ("in build equation", equation)
    return equation

def displayEquation(equation,display):
    display.setText(equation)
    pass

def main():

    #Draw the interface
    win= GraphWin('Calculator',280,360)
    win.setBackground("royal blue")
    
    buttons = [[16,260,20,80,"","light cyan"], [20,60,100,140,"7","dark blue"],[20,60,150,190,"4","dark blue"],[20,60,200,240,"1","dark blue"],
               [20,60,250,290,'+/-',"orange"], [70,110,100,140,"8","dark blue"],[70,110,150,190,"5","dark blue"],[70,110,200,240,"2","dark blue"],
               [70,110,250,290,"0","dark blue"],[120,160,100,140,"9","dark blue"],[120,160,150,190,"6","dark blue"],[120,160,200,240, "3","dark blue"],
               [120,160,250,290,'.',"orange"], [170,210,100,140," + ","orange"],[170,210,150,190," - ","orange"],[170,210,200,240," * ","orange"],
               [170,210,250,290," / ","orange"], [220,260,100,140,'M+',"gray"],[220,260,150,190,'M-',"gray"],[220,260,200,240,'MR',"gray"],[220,260,250,290,'MC',"gray"],
               [170,210,300,340,'Del',"dark orange"],[220,260,300,340,'=',"green"], [120,160,300,340,'AC',"red"]
               ]
    #calling the function drawKeypad in order to scketch the buttons
    drawKeypad(buttons,win)
    memory= 0
    equation = ""
    display= createdisplay(win)
   
    while True:
        click = win.getMouse()
        label = getLabel(buttons,click)
        
        if label == '=':
            equation = solveEquation(equation)
            label=""
            

        elif label == 'AC':
            equation=""

        elif label == 'Del':
            equation= equation[:len(equation)-1]
            
        elif label == '+/-':
            result = float(solveEquation(equation))*-1
            equation=""
            equation= equation + str(result)

        elif label == 'M+':
            memory = memory + float(solveEquation(equation))

        elif label == 'M-':
            memory= memory - float(solveEquation(equation))

        elif label == 'MR':
            
            equation= equation + str (memory)

        elif label == 'MC':
            memory=0

        else: 
    
            after = buildEquation(equation,label)
            equation= "" 
            equation= equation + after
        displayEquation(equation,display)
        




main()
