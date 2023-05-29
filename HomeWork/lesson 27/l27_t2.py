"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом координат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Вектор: {self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)