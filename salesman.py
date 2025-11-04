class Salesman:
    def __init__(self, array_of_cities):
        self.array_of_cities = array_of_cities
        self.current = 0
        self.x = array_of_cities[self.current].x
        self.y = array_of_cities[self.current].y

    def advance(self):
        self.current += 1
        self.x = self.array_of_cities[self.current].x
        self.y = self.array_of_cities[self.current].y