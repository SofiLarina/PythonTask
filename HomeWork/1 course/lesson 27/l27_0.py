class Cars:
    def __init__(self, doors, windows):
        self.doors = doors
        self.windows = windows

    def __gt__(self, other):
        return True if self.doors > other.doors else True

    def __str__(self):
        return f"Я машина у меня {self.doors} двери"

    def __add__(self, other):
        return self.doors + other.doors

#    def __radd__(self, other):
#        return other.doors + self.doors

    def __int__(self):
        return self.doors

Toyota = Cars(4, 6)
Gazel = Cars(3, 10)
print(Toyota > Gazel)
print(Toyota)
print(Toyota + Gazel)
print(Gazel + Toyota)
print(int(Toyota))