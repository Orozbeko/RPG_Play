class Transport:
    def __init__(self, the_model, the_color, the_year):
        # attribututes / fields
        self.model = the_model
        self.color = the_color
        self.year = the_year

    def change_color(self, new_color):
        self.color = new_color

class Plane(Transport):
    def __init__(self, the_model, the_color, the_year):
       super().__init__(the_model, the_color, the_year)
class Car:
    counter = 0
    # constructor                          parametrs
    def __init__(self, the_model, the_color, the_year, penalties=0):
        # attribututes / fields
        self.model = the_model
        self.color = the_color
        self.year = the_year
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f"Car {self.model} is driving to {city}")
    def signal(self, number_of_times, sound):
        sound+=(' ')
        print(f"Car {self.model} makes signal: {sound * number_of_times}")

class Truck(Car):
    def __init__(self, the_model, the_color, the_year, load_capacity):
        super().__init__(the_model, the_color, the_year)
        self.load_capacity = load_capacity

    def load_cargo(self, type_of_cargo, weight):
        if weight > self.load_capacity:
            print(f"You can not load more than {self.load_capacity} kg.")
        else:
            print(f"You successfully load cargo of {type_of_cargo} kg.")


print(f"Factory CAR produced {Car.counter}")

my_nuber = 45
print(my_nuber)
bmw_car = Car("BMW X7", "blue", "2019", penalties=789)
print(bmw_car)
print(f"Model: {bmw_car.model} Color: {bmw_car.color} Year: {bmw_car.year} "
      f"Penalties: {bmw_car.penalties}")

Honda_car = Car(penalties=900, the_color="red", the_year=2009, the_model="Honda Fit")
print(f"Model: {Honda_car.model} Color: {Honda_car.color} Year: {Honda_car.year} "
      f"Penalties: {Honda_car.penalties}")
# Honda_car.color = "green"
Honda_car.change_color("green")
bmw_car.drive('Talas')
bmw_car.signal(3, 'beep')
print(f"Factory CAR produced {Car.counter}")

boeing_plane = Plane("Boeing f-45", 'white', 2016)
print(f"Model: {boeing_plane.model} Color: {boeing_plane.color} Year: {boeing_plane.year}")

kamaz_truck = Truck("Kamaz Daf", 'gray', 2007, 35000)
print(f"Model: {kamaz_truck.model} Color: {kamaz_truck.color} Year: {kamaz_truck.year}"
      f" Load Capacity: {kamaz_truck.load_capacity}")
kamaz_truck.load_cargo('potatoes', 40000)
kamaz_truck.load_cargo('apple', 20000)
kamaz_truck.drive('Osh')
