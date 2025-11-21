from city import *
from math import sqrt

def check_distance(city_1: City, city_2: City) -> float:

    ##Check the distance between cities using the distance formula.
    distance = sqrt((city_1.x - city_2.x)**2 + (city_1.y - city_2.y)**2)
    return distance

def print_cities(list: list[City]):
    for i in range(0, len(list)):
        print(list[i].identifier)

def index_of_next_city(city: City, list_of_cities: list[City]):
    index = 0
    optimal_distance = check_distance(city, list_of_cities[0])
    for i in range(1, len(list_of_cities)):
        distance = check_distance(city, list_of_cities[i])
        if distance < optimal_distance:
            index = i
            optimal_distance = distance
    
    return index

#Must have at least one city in cities
def determine_optimal_path(cities: list[City]) -> list[City]:
    city_list = cities.copy()
    estimated_shortest_path = [city_list.pop(0)]
    
    while len(city_list) > 0:
        index = index_of_next_city(estimated_shortest_path[-1], city_list)
        estimated_shortest_path.append(city_list.pop(index))
    
    estimated_shortest_path.append(estimated_shortest_path[0])

    
    return estimated_shortest_path

