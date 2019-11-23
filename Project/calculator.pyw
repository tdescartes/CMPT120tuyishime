# CMPT 120 Intro to Programming
# Project #2 – Calculator Graphics
# Created: 2019-10-17

# JA: Your memory functions don't seem to be working properly
from graphics import*
from calc_functions import calculate


'''

def memory( result,n):
    if (n==0):
        memory=0
    if (n==1) :
        memory=results
'''      
        

def main():
    
    win= GraphWin("Calculator",280, 360)
    win.setBackground("dark blue")
    
    #Draw the interface
    
    screen=Rectangle(Point(16,20), Point(260,80))
    screen.draw(win)
    screen.setFill('light cyan')

    # column one
    
    seven=Rectangle( Point(20,100), Point(60,140))
    seven.draw(win)
    seven.setFill('light blue')
    
    four=Rectangle( Point(20,150), Point(60,190))
    four.draw(win)
    four.setFill('light blue')
    
    one=Rectangle( Point(20,200), Point(60,240))
    one.draw(win)
    one.setFill('light blue')

    plusorminus=Rectangle( Point(20,250), Point(60,290))
    plusorminus.draw(win)
    plusorminus.setFill('orange')

    #column two

    eight=Rectangle( Point(70,100), Point(110,140))
    eight.draw(win)
    eight.setFill('light blue')
    
    five=Rectangle( Point(70,150), Point(110,190))
    five.draw(win)
    five.setFill('light blue')
    
    two=Rectangle( Point(70,200), Point(110,240))
    two.draw(win)
    two.setFill('light blue')

    zero=Rectangle( Point(70,250), Point(110,290))
    zero.draw(win)
    zero.setFill('light blue')
    
    # column three

    nine=Rectangle( Point(120,100), Point(160,140))
    nine.draw(win)
    nine.setFill('light blue')
    
    six=Rectangle( Point(120,150), Point(160,190))
    six.draw(win)
    six.setFill('light blue')
    
    three=Rectangle( Point(120,200), Point(160,240))
    three.draw(win)
    three.setFill('light blue')

    dot=Rectangle( Point(120,250), Point(160,290))
    dot.draw(win)
    dot.setFill('orange')



    #column four

    division=Rectangle( Point(170,100), Point(210,140))
    division.draw(win)
    division.setFill('orange')
    
    multiplication=Rectangle( Point(170,150), Point(210,190))
    multiplication.draw(win)
    multiplication.setFill('orange')
    
    addition=Rectangle( Point(170,200), Point(210,240))
    addition.draw(win)
    addition.setFill('orange')

    substraction=Rectangle( Point(170,250), Point(210,290))
    substraction.draw(win)
    substraction.setFill('orange')

    delete=Rectangle( Point(170,300), Point(210,340))
    delete.draw(win)
    delete.setFill('orange')

    #column five

    division=Rectangle( Point(220,100), Point(260,140))
    division.draw(win)
    division.setFill('gray')
    
    multiplication=Rectangle( Point(220,150), Point(260,190))
    multiplication.draw(win)
    multiplication.setFill('gray')
    
    addition=Rectangle( Point(220,200), Point(260,240))
    addition.draw(win)
    addition.setFill('gray')

    substraction=Rectangle( Point(220,250), Point(260,290))
    substraction.draw(win)
    substraction.setFill('gray')
    
    equality=Rectangle( Point(220,300), Point(260,340))
    equality.draw(win)
    equality.setFill('Green')


    #Creating buttons for messages
    # column one button
    
    buttonseven=Text( Point(40,120),"7")
    buttonseven.draw(win)
    buttonseven.setTextColor("white")
    buttonseven.setSize(18)
    
   
    buttonfour=Text( Point(40,170), "4")
    buttonfour.draw(win)
    buttonfour.setTextColor("white")
    buttonfour.setSize(18)
    
    buttonone=Text( Point(40,220), "1")
    buttonone.draw(win)
    buttonone.setTextColor("white")
    buttonone.setSize(18)

    buttonplusorminus=Text( Point(40,270), "+/-")
    buttonplusorminus.draw(win)
    buttonplusorminus.setTextColor("white")
    buttonplusorminus.setSize(18)

    #column two button

    buttoneight=Text( Point(90,120), "8")
    buttoneight.draw(win)
    buttoneight.setTextColor("white")
    buttoneight.setSize(18)
    
    buttonfive=Text( Point(90,170), "5")
    buttonfive.draw(win)
    buttonfive.setTextColor("white")
    buttonfive.setSize(18)
    
    buttontwo=Text( Point(90,220), "2")
    buttontwo.draw(win)
    buttontwo.setTextColor("white")
    buttontwo.setSize(18)

    buttonzero=Text( Point(90,270),"0")
    buttonzero.draw(win)
    buttonzero.setTextColor("white")
    buttonzero.setSize(18)
    
    # column three button

    buttonnine=Text( Point(140,120), "9")
    buttonnine.draw(win)
    buttonnine.setTextColor("white")
    buttonnine.setSize(18)
    
    buttonsix=Text( Point(140,170), "6")
    buttonsix.draw(win)
    buttonsix.setTextColor("white")
    buttonsix.setSize(18)
    
    buttonthree=Text( Point(140,220), "3")
    buttonthree.draw(win)
    buttonthree.setTextColor("white")
    buttonthree.setSize(18)

    buttondot=Text( Point(140,270), ".")
    buttondot.draw(win)
    buttondot.setTextColor("white")
    buttondot.setSize(18)

    #column four button

    buttondivision=Text( Point(190,120), "/")
    buttondivision.draw(win)
    buttondivision.setTextColor("white")
    buttondivision.setSize(18)
    
    buttonmultiplication=Text( Point(190,170), "x")
    buttonmultiplication.draw(win)
    buttonmultiplication.setTextColor("white")
    buttonmultiplication.setSize(18)
    
    buttonaddition=Text( Point(190,220), "+")
    buttonaddition.draw(win)
    buttonaddition.setTextColor("white")
    buttonaddition.setSize(18)   

    buttonsubstraction=Text( Point(190,270), "-")
    buttonsubstraction.draw(win)
    buttonsubstraction.setTextColor("white")
    buttonsubstraction.setSize(18)

    buttondelete=Text( Point(190,320), "Del")
    buttondelete.draw(win)
    buttondelete.setTextColor("white")
    buttondelete.setSize(18)

    # column five button

    buttonnine=Text( Point(240,120), "M+")
    buttonnine.draw(win)
    buttonnine.setTextColor("white")
    buttonnine.setSize(18)
    
    buttonsix=Text( Point(240,170), "M-")
    buttonsix.draw(win)
    buttonsix.setTextColor("white")
    buttonsix.setSize(18)
    
    buttonthree=Text( Point(240,220), "MR")
    buttonthree.draw(win)
    buttonthree.setTextColor("white")
    buttonthree.setSize(18)

    buttondot=Text( Point(240,270), "MC")
    buttondot.draw(win)
    buttondot.setTextColor("white")
    buttondot.setSize(18)

    buttonequality=Text( Point(240,320), "=")
    buttonequality.draw(win)
    buttonequality.setTextColor("white")
    buttonequality.setSize(18)


    equation=""
        
    output=Text( Point(115,50), "")
    output.draw(win)
    output.setSize(18)


    #the following are going to be about making this functionality work
    
    while True:
        mouse = win.getMouse()   # getting where the user clicks

        # selecting the x and y coordinates that matches the buttons
        
        #selecting buttons by column1
        if 20 < mouse.x < 60 and 100 < mouse.y < 140:
            equation= equation + "7"
            output.setText(equation)
        
        if 20 < mouse.x < 60 and 150 < mouse.y < 190:
            equation= equation + "4"
            output.setText(equation)
            
        if 20 < mouse.x < 60 and 200 < mouse.y < 240:
            equation= equation + "1"
            output.setText(equation)
    
        if 20 < mouse.x < 60 and 250 < mouse.y < 290:

            mylist= equation.split(" ")
            temp= float (mylist[len(mylist)-1])
            temp= temp * -1
            mylist[len(mylist)-1]= str(temp)
            equation=""
            
            for i in mylist:
                
                equation= equation + " "+ str(i)
        
            output.setText(equation)

        #column2
        
        if 70 < mouse.x < 110 and 100 < mouse.y < 140:
            equation= equation + "8"
            output.setText(equation)
            
        if 70 < mouse.x < 110 and 150 < mouse.y < 190:
            equation= equation + "5"
            output.setText(equation)
            
        if 70 < mouse.x < 110 and 200 < mouse.y < 240:
            equation= equation + "2"
            output.setText(equation)
            
        if 70 < mouse.x < 110 and 250 < mouse.y < 290:
            equation= equation + "0"
            output.setText(equation)

         #column3
            
        if 120 < mouse.x < 160 and 100 < mouse.y < 140:
            equation= equation + "9"
            output.setText(equation)
            
        if 120 < mouse.x < 160 and 150 < mouse.y < 190:
            equation= equation + "6"
            output.setText(equation)
            
        if 120 < mouse.x < 160 and 200 < mouse.y < 240:
            equation= equation + "3"
            output.setText(equation)
            
        if 120 < mouse.x < 160 and 250 < mouse.y < 290:
            equation= equation + "."
            output.setText(equation)


        #column4

        if 170 < mouse.x < 210 and 100 < mouse.y < 140:
            equation= equation + " / "
            output.setText(equation)
            
        if 170 < mouse.x < 210 and 150 < mouse.y < 190:
            equation= equation + " * "
            output.setText(equation)
            
        if 170 < mouse.x < 210 and 200 < mouse.y < 240:
            equation= equation + " + "
            output.setText(equation)
            
        if 170 < mouse.x < 210 and 250 < mouse.y < 290:
            equation= equation + " - "
            output.setText(equation)

        if 170 < mouse.x < 210 and 300 < mouse.y < 340:
            equation= equation[:len(equation)-1]
            output.setText(equation)
            #equation= ""
            #output.setText(equation)


        #column5
        if 220 < mouse.x < 260 and 100 < mouse.y < 140:
            memory=calculate(equation)
            output.setText(equation)
            
        if 220 < mouse.x < 260 and 150 < mouse.y < 190:
             memory=calculate(equation)
             output.setText(equation)
            
        if 220 < mouse.x < 260 and 200 < mouse.y < 240:
            output.setText(equation)
            
        if 220 < mouse.x < 260 and 250 < mouse.y < 290:
            memory=""
            output.setText(equation)
        
        #  for equal
        
        if 220 < mouse.x < 260 and 300 < mouse.y < 340:
            final=calculate(equation)
            output.setText(final)
            equation= ""
            equation= equation + str(final)
            memory
main()
