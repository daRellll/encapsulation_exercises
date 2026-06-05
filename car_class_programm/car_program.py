from car_class import Car

car = Car(2022, "TOYOTA")

for i in range(5):
    car.accelerate()
    print(car.get_speed())