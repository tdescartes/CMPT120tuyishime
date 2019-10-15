# CMPT 120 Intro to Programming
# Project #2 – Calculator
# Created: 2019-10-17


def main():
    
    myanswer= "Lion"

    guess= (input ("Think of an animal, guess what it is: ")).lower()

    while True:

        if guess[0]=="q":

            break

        elif myanswer.lower()!=guess:

            print ("Unfortunately, you missed. Try again Please")
            
            guess= input ("I am Thinking of an animal, guess what it is: ")

        else:
            print ("Congratulation!! You finally got it correct!")
            
            break

    
main()
