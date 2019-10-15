# CMPT 120 Intro to Programming
# Project #2 – Calculator
# Created: 2019-10-17


def main():
    myanswer= "Lion"

    guess= input ("Think of an animal, guess what it is: ")

    while True:

        if myanswer.lower()!=guess.lower():

            print ("Unfortunately, you missed. Try again Please")
            
            guess= input ("I am Thinking of an animal, guess what it is: ")

        else:
            break

    print ("Congratulation!! You finally managed to get it correct!")


main()
