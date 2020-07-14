class Car:
    year = None
    make = None
    model = None
    color = None
    convertible = None
    engine = None
    transmission = None
    top_speed = None
    mileage = 0
    mph = 0

    def __init__(self, year, make, model,
                 color):
        self.year = year
        self.make = make
        self.model = model
        self.color = color

    def accelerate(self, mph, direction="forward"):
        self.mph += mph

    def brake(self, pct):
        self.mph *= pct

    def turn(self):
        pass

    def shift(self):
        pass

    def current_speed(self):
        return self.mph

    def __repr__(self):
        return f"{self.year} {self.make} {self.model}, {self.color}"

    def __eq__(self, other):
        return self.year == other.year \
               and self.make == other.make \
               and self.model == other.model \
               and self.color == other.color

    def __sizeof__(self):
        return 3
