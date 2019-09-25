# The program for fibonacci sequesnce

def fibbo(n):

    n1=0
    n2=1

    for i in range (1,n):
        n3= n1+n2
        n1=n2
        n2=n3
    return n3 

def main():

    n= eval(input("Enter a number: "))

    print ("The Nth fibonacci number is : ", fibbo(n))

main()
