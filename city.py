from random import random

class City:
    def __init__(self, identifier, x: int, y: int):
        self.identifier = identifier
        self.x = x
        self.y = y

def generate_cities(n: int, x_multiplier: int, y_multiplier: int):
    cities = []
    
    for i in range(0, n):
        city = City(i, x_multiplier * random(), y_multiplier * random())
        cities.append(city)

    return cities
