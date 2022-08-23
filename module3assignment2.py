class Car:

    def __init__(self, make, model, colour, year, speed = 5):

        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.speed = speed

    def show_description(self):
        print("This is a", self.colour, self.make)

    def accelerate(self):
        self.speed += 1

    def brake(self):
        self.speed -= 1

    def change_colour(self, colour):
        self.colour = colour

    def change_model(self, model):
        self.model = model

my_car = Car("BMW", "X5", "Black", 2018)
print(type(my_car))

my_car.show_description()

my_car.accelerate()
print(my_car.speed)

my_car.brake()
print(my_car.speed)

my_car.change_colour("Silver")
print(my_car.colour)

my_car.change_model("X6")
print(my_car.model)