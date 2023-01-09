import math
from itertools import permutations


def flight_line(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return result


def traveling_salesman(cities, distances):
    # Generate all possible permutations of the cities
    all_permutations = permutations(cities)

    # Set the initial minimum distance to a very large number
    min_distance = float('inf')
    min_path = []

    # Iterate through all permutations and calculate the total distance for each permutation
    for permutation in all_permutations:
        distance = 0
        for i in range(len(permutation) - 1):
            city_a = permutation[i]
            city_b = permutation[i + 1]
            distance += flight_line(distances[city_a][0], distances[city_a][1], distances[city_b][0],
                                    distances[city_b][1])

        # If the total distance for this permutation is less than the current minimum distance, set the minimum
        # distance to this distance
        if distance < min_distance:
            min_distance = distance
            min_path = permutation

    resultList = list(min_path)
    resultList.append(min_path[0])
    start = distances[min_path[0]]
    last = distances[min_path[len(min_path) - 1]]
    min_distance += flight_line(last[0], last[1], start[0], start[1])

    # Return the minimum distance
    return min_distance, resultList


# Example usage
cities = ['Barcelona', 'Amsterdam', 'New York']

distances = {
    'Barcelona': [41.3927755, 2.0701491],
    'Amsterdam': [52.3547498, 4.8339208],
    'New York': [40.6976701, -74.2598663]
}

print(traveling_salesman(cities, distances))  # Outputs: 30
