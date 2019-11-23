# CMPT 120 Intro to Programming
# Project #1 – Calculator Vo1
# Created: 2019-10-15

def calculate(string1):
    
    mylist= string1.split(" ")
    length= len(mylist)
    
# Added a case for length of mylist equal to 1
    if length == 1:
        temp= float (mylist[0])
        mylist[0]= temp
        return mylist[0]

    else: 

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
                if mylist[index]== "-":
                    index= mylist.index("-")
                    temp= float (mylist[index-1]) - float (mylist[index+1])
                    mylist[index]= temp
                    del mylist[index-1]
                    del mylist[index]
                else:
                    continue
            
            length= len(mylist)
        
        return mylist[0]

