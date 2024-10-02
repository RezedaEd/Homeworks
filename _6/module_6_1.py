class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True

class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print (f'{self.name} не стал есть {food.name}.')
            self.alive = False
class Mammal(Animal):
    pass
class Predator(Animal):
    pass


a1 = Predator('Лев')
a2 = Mammal('Обезъяна')
p1 = Flower('Пион')
p2 = Fruit('Апельсин')

print(a1.name)
print(p1.name, p1.edible)

print(a1.alive, a1.fed)
print(a2.alive, a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive, a1.fed)
print(a2.alive, a2.fed)
