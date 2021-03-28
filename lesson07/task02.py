from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, size: float, height: float):
        self.size = size
        self.height = height

    @abstractmethod
    def get_area(self):
        pass


class Coat(Clothing):
    def __init__(self, size, height=0):
        super().__init__(size, height)

    @property
    def get_area(self):
        return self.size / 6.5 + 0.5


class Jacket(Clothing):
    def __init__(self, height, size=0):
        super().__init__(size, height)

    @property
    def get_area(self):
        return self.height * 2 + 0.3


coat = Coat(13)
jacket = Jacket(10)
print(f"Расход ткани на пальто: {coat.get_area}")
print(f"Расход ткани на пиджак: {jacket.get_area}")
print(f"Суммарный расход ткани: {coat.get_area + jacket.get_area}")
