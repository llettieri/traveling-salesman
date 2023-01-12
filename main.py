import json
import math
from itertools import permutations
import pandas as pd

file = open('cities.json')
pd.DataFrame = json.load(file)
data = pd.DataFrame

continent = pd.Series(["continent"])


cities = ['Barcelona', 'Amsterdam', 'New York', 'Zürich']

print("Welchen Kontinent wollen sie bereisen? ")
print("Hallo diese Städte bieten wir dir an und berechnen dir die schnellste Route um diese zu bereisen. ")

input = input("In welche Städte wollen Sie gehen?")


def flight_line(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return result

def traveling_salesman(cities, distances):

    all_permutations = permutations(cities)

    min_distance = float('inf')
    min_path = []

    for permutation in all_permutations:
        distance = 0
        for i in range(len(permutation) - 1):
            city_a = permutation[i]
            city_b = permutation[i + 1]
            distance += flight_line(distances[city_a][0], distances[city_a][1], distances[city_b][0],
                                    distances[city_b][1])

        if distance < min_distance:
            min_distance = distance
            min_path = permutation

    resultList = list(min_path)
    resultList.append(min_path[0])
    start = distances[min_path[0]]
    last = distances[min_path[len(min_path) - 1]]
    min_distance += flight_line(last[0], last[1], start[0], start[1])

    return min_distance, resultList

cities = ['Barcelona', 'Amsterdam', 'New York', 'Zürich']

distances = {
    'Barcelona': [41.3927755, 2.0701491],
    'Amsterdam': [52.3547498, 4.8339208],
    'New York': [40.6976701, -74.2598663],
    'Zürich': [47.3775366, 8.4666957]
}

print(traveling_salesman(cities, distances))  # Outputs: 30
