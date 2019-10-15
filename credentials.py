#   CMPT 120 Intro to Programming
#   Lab #4 -- Working with strings and Functions
#   Created: 2019-10-01

#This fucntion is for gathering names.
import array as arr
def getnames():

        first= input ("Enter your first name: ")
        last= input ("Enter your last name: ")
        return (first + " "+last)

# This function is for creating Marist Style username in lowercase
def maristyle(fulname):

    first,last=fulname.split(" ")
    username= first.lower()+"."+ last.lower()

    return username

#function is for getting and checking the strength of a password from the user

def getpaswd():

    passwd= input ("Create a new password: ")

    iStrong(passwd)
    while (iStrong(passwd)== False):
        print ("Fool of a Took! That password is feeble!")
        passwd= input ("Try a new password with a number, capital,and lowercase: ")
        iStrong(passwd)  
#    else:
    print ("The force is strong in this one")
    return (passwd)


#The function that test the strenth of the password from the user
    
def iStrong(passwd):
    if len(passwd)<8:
        return False
    elif passwd.lower()== passwd:
        return False
    elif passwd.upper()== passwd:
        return False
    elif any(char.isdigit() for char in passwd)== False:
        return False
    
    '''elif (passwd.isdigit()== True | type (passwd)==str):
        return False'''
    


def main():
    

    number= eval(input("How many accounts do you want:"))

    for i in range (1,number+1):
        names= getnames()
        usrname= maristyle(nam)
        passwrd= getpaswd()
        colusrname[i]= array[]
        print (" Full name: ", names)
        print (" Your password: ", passwrd)
        print("Account configured. Your new email address is", usrname+ "@marist.edu")


main()
