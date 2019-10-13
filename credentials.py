#   CMPT 120 Intro to Programming
#   Lab #4 -- Working with strings and Functions
#   Created: 2019-10-01


#This fucntion is for gathering names.

def getnames():
    
    first= input ("Enter your first name: ")
    last= input ("Enter your last name: ")
    str=(first + " "+last)
    return str

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
        passwd= input ("Create a new password: ")
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
    


def main():

   
    
    names=getnames()
    usrname= maristyle(names) 
    passwrd= getpaswd()

    print (" Full name: ", names)
    print (" Your password: ", passwrd)
    print("Account configured. Your new email address is", usrname+ "@marist.edu")


main()
