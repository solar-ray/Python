class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'Запуск отрисовки ручкой'


class Pencil(Stationery):

    def draw(self):
        return f'Запуск отрисовки карандашом'


class Handle(Stationery):

    def draw(self):
        return f'Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
