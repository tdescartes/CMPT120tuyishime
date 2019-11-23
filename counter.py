# Introduction to Programming
# Lab#9 - Working with Objects and Inheritance
# Author: Descartes Tuyishime
# Date: 11-19-2019 


def main():
    my_counter = Counter()
    my_counter.get_value()
    my_counter.increment()
    my_counter.increment()
    my_counter.get_value() 
    my_counter.clear()
    my_counter.get_value()

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self): # increasing the value of the count
        self.count += 1
    def clear(self):
        self.count = 0
    def get_value(self): 
        return self.count




class BankAccount:
    """Bank Account protected by a pin number."""
    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self.balance=0
        self.pin="pin"
    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        if(self.pin== pin):
            self.balance= self.balance + amount
            return self.balance
    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if(self.pin== pin):
            self.balance= self.balance - amount
            return (amount)
        
    def get_balance(self, pin):
        """Return account balance."""
        if(self.pin== pin):
            return self.balance

        
    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        if(self.pin== oldpin):
            self.pin= newpin


main()   
