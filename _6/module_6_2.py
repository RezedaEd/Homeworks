class Vehicle:
    __COLOR_VARIANTS = ['black', 'blue', 'yellow', 'green', 'red', 'white']
    def __init__(self, owner,  model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep='\n')

    def set_color(self, new_color):
        if new_color.casefold() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

p1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
p1.print_info()

p1.owner = 'Paul'
p1.set_color('brown')
p1.set_color('red')
p1.print_info()
