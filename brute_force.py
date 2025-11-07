from itertools import permutations
from city import *
import math


def distance(cities: list[City]) -> float:
    distance = 0.0

    if len(cities) > 1:
        for i in range(0, len(cities) - 1):
            ##Check the distance between each city using the distance formula.
            distance += math.sqrt((cities[i].x - cities[i+1].x)**2 + (cities[i].y - cities[i+1].y)**2)
        ##Check the distance from the last city back to the first.
        distance += math.sqrt((cities[0].x - cities[-1].x)**2 + (cities[0].y - cities[-1].y)**2)
    return distance

def determine_optimal_path(cities: list[City]) -> list[City]:
    ##Get all permutations
    city_permutations = list(permutations(cities))
    
    shortest_path = city_permutations[0]
    shortest_distance = distance(shortest_path)

    ##Check the distance of all permutations, and return the one with the shortest distance.
    for i in range(1, len(city_permutations)):
        current_distance = distance(city_permutations[i])
        if shortest_distance > current_distance:
            shortest_path = city_permutations[i]
            shortest_distance = current_distance

    return shortest_path

def print_cities(list: list[City]):
    for i in range(0, len(list)):
        print(list[i].identifier)

def main():
    cities = generate_cities(10)
    for i in range(0, len(cities)):
        print(f"({cities[i].x}, {cities[i].y})")
    
    path = determine_optimal_path(cities)

    print_cities(path)

if __name__ == "__main__":
    main()