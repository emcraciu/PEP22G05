import time

class Car():
    color = 'yellow'
    motors = ["fw-2KW-engine"]

    def __init__(self, color='red'):
        # print(self.color)
        # wheels = 4 # this is local to __init__
        self.wheels = 4
        self.construction_date = time.time()
        self.color = color


car1 = Car('green')
print(type(car1))
print(car1.color)

time.sleep(1)

car2 = Car()
print(type(car2))
print(car2.color)

car2.color = 'blue'
print("Car2 is :", car2.color)
print("Car1 is :", car1.color)

car2.motors.append("rw-4KW-engine")
print("Car2 motor is :", car2.motors)
print("Car1 motor is :", car1.motors)

car2.wheels = 5
print("Car2 wheels is :", car2.wheels)
print("Car1 wheels is :", car1.wheels)

print("Car2 date is :", car2.construction_date)
print("Car1 date is :", car1.construction_date)