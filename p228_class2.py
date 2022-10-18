from re import M
from tkinter import E


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

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an otometer.")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# 자식 클래스에 상속
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 부모클래스의 속성을 자식인스턴스에 모두 전달
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car battery is " + str(self.battery_size) + '-kwh.')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#부모 클래스 메서드 오버라이드
class ElectricCar2(Car):
    def __init__(self, make, model, year):
        # 부모클래스의 속성을 자식인스턴스에 모두 전달
        super().__init__(make, model, year)
        self.battery_size = 100

    def describe_battery(self):
        print("This car battery is " + str(self.battery_size) + '-kwh.')

    def fill_gas_tank(self):
        print("This car no gas tank")

my_tesla2 = ElectricCar2('tesla2', 'model s2', 2020)
print(my_tesla2.get_descriptive_name())
my_tesla2.describe_battery()
my_tesla2.fill_gas_tank()