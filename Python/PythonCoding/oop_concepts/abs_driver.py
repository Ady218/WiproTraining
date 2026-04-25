from oop_concepts.rectangle import Rectangle
from oop_concepts.square import Square

sqobj = Square(10)

print(f'Area: {sqobj.calculate_area()} \n Perimeter: {sqobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)

print(f'Area: {rectobj.calculate_area()} \n Perimeter: {rectobj.calculate_perimeter()}')