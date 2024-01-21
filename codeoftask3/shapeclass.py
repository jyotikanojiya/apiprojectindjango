class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


c =Circle(2)
print(c.calculate_area())
print(c.calculate_perimeter())


r =Rectangle(11,12)
print(r.calculate_area())
print(r.calculate_perimeter())