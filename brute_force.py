from itertools import permutations
from city import *
import math


def distance(cities: list[City]) -> float:
    total = 0.0

    if len(cities) > 1:
        for i in range(0, len(cities) - 1):
            dx = cities[i].x - cities[i + 1].x
            dy = cities[i].y - cities[i + 1].y
            total += math.sqrt(dx * dx + dy * dy)
        # Return to start
        dx = cities[0].x - cities[-1].x
        dy = cities[0].y - cities[-1].y
        total += math.sqrt(dx * dx + dy * dy)

    return total


def determine_optimal_path(cities: list[City]) -> list[City]:
    n = len(cities)

    if n <= 1:
        # Nothing to optimize, just return copy
        return cities.copy()

    # Fix the starting city
    start = cities[0]
    #Rest of the cities in new list
    other_cities = cities[1:]

    shortest_path: list[City]
    shortest_distance = float.inf

    # Iterate over permutations
    for perm in permutations(other_cities):
        #Unpack the permutations of the remaining cities after the starting city at index zero
        candidate_path = [start, *perm]

        current_distance = distance(candidate_path)

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            # Copy so we do not mutate the same list later
            shortest_path = list(candidate_path)

    # Close the loop for output: repeat the start at the end
    shortest_path.append(start)

    return shortest_path
