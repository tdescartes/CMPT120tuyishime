# CMPT 120 Intro to Programming
# Lab #8 -  Lists and Error Handling
# Author: Descartes Tuyishime
# Created: 2019-Nov-12

productNames = [ "Ultrasonic range finder"
 , "Servo motor"
 , "Servo controller"
 , "Microcontroller Board"
 , "Laser range finder"
 , "Lithium polymer battery"
 ]

productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")",productNames[i], "$", productPrices[i])
            print()

            
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodId = int(vals[0])
        count = int(vals[1])
        if productQuantities[prodId] >= count:
            if cash >= productPrices[prodId]:
                productQuantities[prodId] -= count
                cash -= productPrices[prodId] * count
                print("You purchased", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productNames[prodId])
main()
