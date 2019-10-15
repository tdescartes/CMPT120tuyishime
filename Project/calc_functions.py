# CMPT 120 Intro to Programming
# Project #1 – Calculator Vo1
# Created: 2019-10-15

def main():

    string1= input ("Enter you calculation: ")
    mylist= string1.split(" ")
    length= len(mylist)

    # The look to search and use operator
    while length > 1:
        if "*" in mylist:
            temp= float (mylist[length-1]) * float (mylist[length+1])
            mylist[i]= temp
            del mylist[length-1]
            del mylist[length+1]
            
        elif "/" in mylist:
            temp= float (mylist[length-1]) / float (mylist[length+1])
            mylist[i]= temp
            del mylist[length-1]
            del mylist[length+1]

        elif "+" in mylist:
            temp= float (mylist[length-1]) + float (mylist[length+1])
            mylist[i]= temp
            del mylist[length-1]
            del mylist[length+1]

        elif "-" in mylist:
            temp= float (mylist[length-1]) - float (mylist[length+1])
            mylist[i]= temp
            del mylist[length-1]
            del mylist[length+1]
            
        length= len (length)

    print ("The results is", mylist[0] )


main()
