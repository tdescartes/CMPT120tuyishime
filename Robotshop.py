# CMPT 120 Intro to Programming
# Lab #8 -  Lists and Error Handling
# Author: Descartes Tuyishime
# Created: 2019-Nov-12




class Product:

    def __init__(self, name, price, quantity):
        self.name= name
        self.price = price
        self.quantity = quantity

    def getname(self):
        return self.name

    def getprice(self):
        return self.price
    
    def getquantity(self):
        return self.quantity
    

    def checkout(self, count):

        if self.quantity >= count:
            return True
        else:
            return False

    def totalcost(self, count):
        return self.price * count


    def pquantity(self,count):
        self.quantity -= count

        

products = [Product(" Ultrasonic range finder", 2.50,4),
            Product(" Servo motor", 14.99, 10),
            Product(" Servo controller", 44.95, 5),
            Product(" Microcontroller Board", 34.95, 7),
            Product(" Laser range finder", 149.99, 2 ),
            Product(" Lithium polymer battery", 8.99, 8) ]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].checkout(1):
            print( i+1,")", products[i].getname(), "$", products[i].getprice())
            print()

            
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodId = int(vals[0])-1
        count = int(vals[1])
        product = products[prodId]

        if product.checkout(count):
            if cash >= product.totalcost(count):
                product.pquantity(count)
                cash -= product.totalcost(count)
                print("You purchased", count, product.name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.getname())

main()
