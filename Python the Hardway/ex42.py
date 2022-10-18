class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

rollingstone = Dog("rollingstone!!!")
print(rollingstone.name)
devil = Cat("devil!!!")

class Human(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

Younghee = Human("Younghee!!!")
print(Younghee.name)

class Workder(Human):
    def __init__(selfself, name, wage):
        super(Workder, self)._init__(name)
        self.wage = wage


