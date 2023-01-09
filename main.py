from itertools import permutations


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
            distance += distances[city_a][city_b]

        # If the total distance for this permutation is less than the current minimum distance, set the minimum
        # distance to this distance
        if distance < min_distance:
            min_distance = distance
            min_path = permutation

    # Return the minimum distance
    return min_distance, list(min_path)


# Example usage
cities = ['A', 'B', 'C', 'D']
distances = {
    'A': {'B': 70, 'C': 65, 'D': 25},
    'B': {'A': 70, 'C': 30, 'D': 100},
    'C': {'A': 65, 'B': 30, 'D': 20},
    'D': {'A': 25, 'B': 100, 'C': 20},
}

print(traveling_salesman(cities, distances))  # Outputs: 30
