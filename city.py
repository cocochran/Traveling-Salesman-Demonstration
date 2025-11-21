from random import random
from math import floor

class City:
    def __init__(self, identifier, x: int, y: int):
        self.identifier = identifier
        self.x = x
        self.y = y

def generate_cities(n: int, x_multiplier: int, y_multiplier: int):
    cities = []
    
    #Possible names to generate
    possible_names = ["Paris", "London", "New York", "Shanghai", "Moscow", "Cape Town", "Mexico City", "Cairo", "Karnaca", "Dunwall"]
    for i in range(0, n):
        #If names left, give the cities generated a name.
        if (len(possible_names) > 0):
            name = possible_names.pop(floor(len(possible_names) * random()))
            city = City(name, x_multiplier * random(), y_multiplier * random())
        #If no names are left, start giving them number identifiers.
        else:
            city = City(f"{i}", x_multiplier * random(), y_multiplier * random())

        cities.append(city)

    return cities
    


