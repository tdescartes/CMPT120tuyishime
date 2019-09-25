#the program that estimates the the pi

import math

def calculate(n):
    sum=0
    i= 1
    sign = 1
    for i in range (1,2*n+1,2):
        sum += sign*4/i
        sign = -sign

    return sum

def main():
    n= eval(input("Enter number of terms to sum: "))

    accuracy=calculate(n)- math.pi
    print ("The math.pi is equal= ", math.pi)
    print ("The pi I calculated is ", calculate(n))
    
    print("The accuracy error of my pi program is", accuracy)


main()
