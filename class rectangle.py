#write a class called rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
#method that will compute the area and the perimeter
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# sample:
length = 44
width = 88
my_rectangle = Rectangle(length, width)
#print the area and the perimeter of the rectangle
print("Area of the rectangle:", my_rectangle.area())
print("Perimeter of the rectangle:", my_rectangle.perimeter())
