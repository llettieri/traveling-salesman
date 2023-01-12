import json
import math
from itertools import permutations


def calc_flight_line(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return result


def traveling_salesman(cities):
    cityNames = []
    distances = {}

    for city in cities:
        cityNames.append(city['name'])
        distances.update({city['name']: [city['x'], city['y']]})

    # Generate all possible permutations of the cities
    fixed_start = cityNames[0];
    rest_destinations = cityNames[:0] + cityNames[1:]
    all_permutations = permutations(rest_destinations)

    # Set the initial minimum distance to a very large number
    min_distance = float('inf')
    min_path = []

    # Iterate through all permutations and calculate the total distance for each permutation
    for permutation in all_permutations:
        distance = 0
        combination = (fixed_start,) + permutation

        for i in range(len(combination) - 1):
            city_a = combination[i]
            city_b = combination[i + 1]

            distance += calc_flight_line(distances[city_a][0], distances[city_a][1], distances[city_b][0],
                                         distances[city_b][1])

        # If the total distance for this permutation is less than the current minimum distance, set the minimum
        # distance to this distance
        if distance < min_distance:
            min_distance = distance
            min_path = combination

    resultList = list(min_path)
    resultList.append(min_path[0])
    start = distances[min_path[0]]
    last = distances[min_path[len(min_path) - 1]]
    min_distance += calc_flight_line(last[0], last[1], start[0], start[1])

    # Return the minimum distance
    return min_distance, resultList


data = json.load(open('cities.json'))

europe = data['continents']['Europe']
northAmerica = data['continents']['North America']


continentInput = input("Which continent do you want to visit?  1 = Europe, 2 = North America: ")
selectedContinent = []

if continentInput == '1':
    selectedContinent = europe
elif continentInput == '2':
    selectedContinent = northAmerica
else:
    print("No valid continent!")
    exit(1)

for city in selectedContinent:
    print(city['id'], city['name'])

cityInput = input("Which cities would you like to visit (comma separated)?: ")
selectedCities = cityInput.replace(' ', '').split(',')
cities = []


for selection in selectedCities:
    for city in selectedContinent:
        if str(city['id']) == selection:
            cities.append(city)

start = input("Define your start city ID: ")
orderedCities = cities.copy()
for city in cities:
    if str(city['id']) == start:
        orderedCities.remove(city)
        orderedCities.insert(0, city)

print(traveling_salesman(orderedCities))
