# родитель, суперкласс
class Car:
    # инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

# дочерний класс, потомок, подкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    # переопределяем метод в дочернем классе. сигнатура должна совпадать
    def drive_to_location(self, location):
        print(f"Bus {self.model} is driving to ")

    # другой метод, которого нет в родительском классе
    def test_bus(self):
        print(f"Bus test {self.color}")


bus_40 = Bus("yellow", "Mercedes Benz", 40)
bus_40.drive_to_location("Bishkek")
print(bus_40.color)

car_honda = Car("black", "Honda Civic")
car_honda.drive_to_location("Karakol")


vehicles = [car_honda, bus_40]
for v in vehicles:
    v.drive_to_location(location="Bishkek")
