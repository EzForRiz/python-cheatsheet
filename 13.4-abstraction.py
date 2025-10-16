# Abstraction in OOP is the process of hiding complex, internal implementation details while exposing only the essential, relevant features to the user. 


# Abstraction example
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass  # Must be implemented by subclasses

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Usage
s = Square(5)
print(s.area())  # Only care about area(), not how it's calculated
