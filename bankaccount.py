# Introduction to Programming
# Lab#9 - Working with Objects and Inheritance
# Author: Descartes Tuyishime
# Date: 11-19-2019 


def main():
    account= BankAccount("pin")
    account.get_balance("pin")
    print("The balance", account.get_balance("pin"))


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

