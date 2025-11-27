class AutoMobile:
    def __init__(self, brea, clac, engine):
        self.colore = ''
        self.brea = brea
        self.clac = clac
        self.engine = engine

    def set_color(self, c):
        self.colore = c

    def get_color(self):
        return self.colore

    def set_engine(self, e):
        self.engine = e

    def get_engine(self):
        return self.engine


class Bike(AutoMobile):
    def __init__(self, brea, clac, engine, gear, wheel, seats):
        super().__init__(brea, clac, engine)
        self.gear = gear
        self.wheel = wheel
        self.seats = seats

    def set_gear(self, g):
        self.gear = g

    def get_gear(self):
        return self.gear

    def set_wheel(self, w):
        self.wheel = w

    def get_wheel(self):
        return self.wheel

    def set_seats(self, s):
        self.seats = s

    def get_seats(self):
        return self.seats


class Car(Bike):
    def __init__(self, brea, clac, engine, gear, revers_gear, wheel, seats, dore,  sun_ruf):
        super().__init__(brea, clac, engine, gear, wheel, seats)
        self.dore = dore
        self.sun_ruf = sun_ruf
        self.revers_gear = revers_gear

    def set_dore(self, d):
        self.dore = d

    def get_dore(self):
        return self.dore

    def set_sun(self, s):
        self.sun = s

    def get_sun(self):
        return self.sun

    def set_sun_ruf(self, sr):
        self.sun_ruf = sr

    def get_sun_ruf(self):
        return self.sun_ruf

    def set_revers_gear(self,):
        self.revers_gear = 1

    def get_revers_gear(self):
        return self.revers_gear



# Example usage
b = Bike('disc brake', 'manual clutch', '500cc', 5, 2, 2)
b.set_color('black')
print("Bike details:")
print("Color:", b.get_color())
print("Brake:", b.brea)
print("Clutch:", b.clac)
print("Engine:", b.get_engine())
print("Gear:", b.get_gear())
print("Wheel:", b.get_wheel())
print("Seats:", b.get_seats())

c = Car('disc brake', 'automatic', '1500cc', 6, 1, 5, 4, 4, 'panoramic')
c.set_color('blue')

print("\nCar details:")
print("Color:", c.get_color())
print("Brake:", c.brea)
print("Clutch:", c.clac)
print("Engine:", c.get_engine())
print("Gear:", c.get_gear())
print("And Revers Gear :", c.get_revers_gear())
print("Wheel:", c.get_wheel())
print("Seats:", c.get_seats())
print("Doors:", c.get_dore())
print("Sunroof Type:", c.get_sun_ruf())
