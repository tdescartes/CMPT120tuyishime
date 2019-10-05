#   CMPT 120 Intro to Programming
#   Lab #4 -- Working with strings and Functions
#   Created: 2019-10-01




#This fucntion is for gathering names.

def getnames():

        first= input ("Enter your first name: ")
        last= input ("Enter your last name: ")
        return (first + " "+last)

# This function is for creating Marist Style username
def maristyle(fulname):

    first,last=fulname.split(" ")
    username= first+"."+ last

    return username

#function is for getting and checking the strength of a password from the user

def getpaswd():

    passwd= input ("Create a new password: ")

    while (len(passwd)<8):
        print ("Fool of a Took! That password is feeble!")
        passwd= input ("Create a new password: ")
    else:
        print ("The force is strong in this one")
        return (passwd)


# Creating a function that builds a Marist 



def main():
    
    
    names=getnames()
    usrname= maristyle(names)

    passwrd= getpaswd()

    print (" Full name: ", names)

    print (" Your password: ", passwrd)


    print("Account configured. Your new email address is", usrname+ "@marist.edu")


main()
