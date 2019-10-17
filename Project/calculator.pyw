# CMPT 120 Intro to Programming
# Project #2 – Calculator Graphics
# Created: 2019-10-17

from graphics import*

def main():
    win= GraphWin("Simple calculator", 230, 360)


    #Draw the interface
    
    screen=Rectangle( Point(16,20), Point(214,80))
    screen.draw(win)

    # column one
    
    seven=Rectangle( Point(20,100), Point(60,140))
    seven.draw(win)
    
    four=Rectangle( Point(20,150), Point(60,190))
    four.draw(win)
    
    one=Rectangle( Point(20,200), Point(60,240))
    one.draw(win)

    plusorminus=Rectangle( Point(20,250), Point(60,290))
    plusorminus.draw(win)

    #column two

    eight=Rectangle( Point(70,100), Point(110,140))
    eight.draw(win)
    
    five=Rectangle( Point(70,150), Point(110,190))
    five.draw(win)
    
    two=Rectangle( Point(70,200), Point(110,240))
    two.draw(win)

    zero=Rectangle( Point(70,250), Point(110,290))
    zero.draw(win)
    
    # column three

    nine=Rectangle( Point(120,100), Point(160,140))
    nine.draw(win)
    
    six=Rectangle( Point(120,150), Point(160,190))
    six.draw(win)
    
    three=Rectangle( Point(120,200), Point(160,240))
    three.draw(win)

    dot=Rectangle( Point(120,250), Point(160,290))
    dot.draw(win)

    delete=Rectangle( Point(120,300), Point(160,340))
    delete.draw(win)

    #column four

    division=Rectangle( Point(170,100), Point(210,140))
    division.draw(win)
    
    multiplication=Rectangle( Point(170,150), Point(210,190))
    multiplication.draw(win)
    
    addition=Rectangle( Point(170,200), Point(210,240))
    addition.draw(win)

    substraction=Rectangle( Point(170,250), Point(210,290))
    substraction.draw(win)

    equality=Rectangle( Point(170,300), Point(210,340))
    equality.draw(win)

    

    #Creating buttons for messages
    # column one button
    
    buttonseven=Text( Point(40,120),"7")
    buttonseven.draw(win)
   
    buttonfour=Text( Point(40,170), "4")
    buttonfour.draw(win)
    
    buttonone=Text( Point(40,220), "1")
    buttonone.draw(win)

    buttonplusorminus=Text( Point(40,270), "+/-")
    buttonplusorminus.draw(win)

    #column two button

    buttoneight=Text( Point(90,120), "8")
    buttoneight.draw(win)
    
    buttonfive=Text( Point(90,170), "5")
    buttonfive.draw(win)
    
    buttontwo=Text( Point(90,220), "2")
    buttontwo.draw(win)

    buttonzero=Text( Point(90,270),"0")
    buttonzero.draw(win)
    
    # column three button

    buttonnine=Text( Point(140,120), "9")
    buttonnine.draw(win)
    
    buttonsix=Text( Point(140,170), "6")
    buttonsix.draw(win)
    
    buttonthree=Text( Point(140,220), "3")
    buttonthree.draw(win)

    buttondot=Text( Point(140,270), ".")
    buttondot.draw(win)

    buttondelete=Text( Point(140,320), "Del")
    buttondelete.draw(win)

    #column four button

    buttondivision=Text( Point(190,120), "/")
    buttondivision.draw(win)
    
    buttonmultiplication=Text( Point(190,170), "X")
    buttonmultiplication.draw(win)
    
    buttonaddition=Text( Point(190,220), "+")
    buttonaddition.draw(win)

    buttonsubstraction=Text( Point(190,270), "-")
    buttonsubstraction.draw(win)

    buttonequality=Text( Point(190,320), "=")
    buttonequality.draw(win)






main()
