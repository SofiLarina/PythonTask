class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def print_info(self):
        print("Дан прямоугольник с длиной", self.length, "и шириной", self.width)
    def perimeter(self):
        return (self.width + self.length) * 2
    def square(self):
        return self.width * self.length
    def check(self, other):
        if self.length < other.length and self.width < other.width:
            print("Треугольник может поместиться в другой")
        else:
            print("Треугольник не может поместиться в другой")
rec1 = Rectangle(5, 10)
rec1.print_info()
print("Периметр прямоугольника: ", rec1.perimeter())
print("Площадь прямоугольника: ", rec1.square())

rec2 = Rectangle(3, 8)
rec2.print_info()
print("Периметр прямоугольника: ", rec2.perimeter())
print("Площадь прямоугольника: ", rec2.square())

rec2.check(rec1)
rec1.check(rec2)