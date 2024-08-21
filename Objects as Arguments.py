class Car:

    color = None

def change_color(car,color):

    car.color = color

car_1 = Car()

change_color(car_1,"red")

print(car_1.color)