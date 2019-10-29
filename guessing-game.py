# CMPT 120 Intro to Programming
# Project #2 – Guessing game
# Created: 2019-10-17


def main():
    
    myanswer= "Lion"

    guess= (input ("I am thinking of an animal, guess what it is: ")).lower()

    while True:

        if guess[0]=="q":

            break

        elif myanswer.lower()!=guess:

            print ("Unfortunately, you missed. Try again Please")
            
            guess= input ("I am Thinking of an animal, guess what it is: ").lower()

        else:
            print ("Congratulation!! You finally got it correct!")

            prefer= input("Do you like it? (Y/N)")

            if (prefer.lower() == "y"):

                print ("Today is your happy day!")

            else:
                 print("Sorry! That's sad to hear!")


            
            break

    
main()
