class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculate_mass(self, mass, thickness):
        return self._length * self._width * mass * thickness / 1000


r = Road(5000, 20)
print(r.calculate_mass(25, 5))
