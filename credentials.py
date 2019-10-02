#   CMPT 120 Intro to Programming
#   Lab #5- Working with strings and Functions
#   Created: 2019-10-01


def main():

    # Getting user's first and last name

    first= input ("Enter your first name: ")
    last= input ("Enter your last name: ")

    # Generating a Marist-style username
    
    uname= first+ (".")+ last

    # Getting and checking user's password

    passwd= input ("Create a new password: ")

    while (len(passwd)<8):
        print ("Fool of a Took! That password is feeble!")
        passwd= input ("Create a new password: ")
    else:
        print ("The force is strong in this one")
        print("Account configured. Your new email address is", uname + "@marist.edu")
    


main()
