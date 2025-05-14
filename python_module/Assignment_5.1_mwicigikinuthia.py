
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
    
    def show_identity(self):
        print(f"I am {self.name}, from {self.origin}, and my power is {self.power}!")

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")


class Speedster(Superhero):
    def __init__(self, name, origin, max_speed):
        super().__init__(name, "Super Speed", origin)
        self.max_speed = max_speed

    def attack(self):
        print(f"{self.name} dashes at {self.max_speed} km/h to attack!")
class Flyer(Superhero):
    def __init__(self, name, origin, flight_altitude):
        super().__init__(name, "Flight", origin)
        self.flight_altitude = flight_altitude

    def attack(self):
        print(f"{self.name} swoops down from {self.flight_altitude} feet to strike!")
