class Cell:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other: 'Cell'):
        return self.quantity + other.quantity

    def __sub__(self, other: 'Cell'):
        if self.quantity < other.quantity:
            return "Вычитание невозможно!"
        else:
            return self.quantity - other.quantity

    def __mul__(self, other: 'Cell'):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other: 'Cell'):
        return self.quantity // other.quantity

    def make_order(self, row_length):
        row = ''
        for i in range(self.quantity // row_length):
            row += f"{'*' * row_length} \n"
        row += f"{'*' * (self.quantity % row_length)}"
        return row


cell1 = Cell(17)
cell2 = Cell(14)
cell3 = cell1 * cell2
print(f"Сложение: {cell1 + cell2}")
print(f"Вычитание: {cell1 - cell2}")
print(f"Умножение: {cell3.quantity}")
print(f"Деление: {cell1 / cell2}")
print(cell1.make_order(5))
