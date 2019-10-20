# CMPT 120 Intro to Programming
# Project #1 – Calculator Vo1
# Created: 2019-10-15

# JA: Move the main() function to calculate.py
def main():

    string1= input ("Enter you calculation: ")
    mylist= string1.split(" ")
    length= len(mylist)
    print(solve(mylist))

def solve(mylist):
    # The look to search and use operator
    while length > 1:
        if "/" in mylist:
            index= mylist.index("/")
            temp= float (mylist[index-1]) / float (mylist[index+1])
            mylist[index]= temp
            del mylist[index-1]
            del mylist[index]
            
        elif "*" in mylist:
            index= mylist.index("*")
            temp= float (mylist[index-1]) * float (mylist[index+1])
            mylist[index]= temp
            del mylist[index-1]
            del mylist[index]

        elif "+" in mylist:
            index= mylist.index("+")
            temp= float (mylist[index-1]) + float (mylist[index+1])
            mylist[index]= temp
            del mylist[index-1]
            del mylist[index]

        elif "-" in mylist:
            index= mylist.index("-")
            temp= float (mylist[index-1]) - float (mylist[index+1])
            mylist[index]= temp
            del mylist[index-1]
            del mylist[index]
            
        length= len(mylist)

#    print ("The results is", mylist[0] )


main()
