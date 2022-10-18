class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting")

    def roll_over(self):
        print(self.name.title() + " roll over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name)
print(str(my_dog.age) + " years old")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name)
print(str(your_dog.age) + " years old")
your_dog.sit()
your_dog.roll_over()


# 클래스 속성 값을 외부에서 직접 접근해서 변경
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + 'miles.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 클래스 속성 값을 변경하는 메소드를 클래스 내부에서 정의
class Car2():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + 'miles.')

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

my_new_car2 = Car2('audi', 'a4', 2016)
print(my_new_car2.get_descriptive_name())
my_new_car2.update_odometer(50)
my_new_car2.read_odometer()
