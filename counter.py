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

           
class DecrementingCounter:
    """Simple counter that can be incremented, decremented, and cleared."""
    def __init__(self):
        """Initialize counter to 0."""
        self.count = 0
    def increment(self):
        """Increment counter by 1."""
        self.count += 1
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1
    def clear(self):
        """Clear counter to 0."""
        self.count = 0
    def get_value(self):
        """Return the current value of the counter."""
        return self.count


class DecrementingCounter2(Counter):
    """Simple counter that can be incremented, decremented, and cleared."""
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1

    
class DecrementingCounter2(Counter):
    """Simple counter that can be incremented, decremented, and cleared."""
    def increment(self):
        """Increment counter by 2."""
        self.count += 2
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1



main()   
