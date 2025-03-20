import math
from typing import List, Tuple
from statistics import mean
import random

class Person:
    # Represents a person's location relative to flag rows.
    def __init__(self, red_distance: float, yellow_distance: float,
                 green_distance: float, blue_distance: float):
        self.red_distance = red_distance
        self.yellow_distance = yellow_distance
        self.green_distance = green_distance
        self.blue_distance = blue_distance

    def get_nearest_distances(self) -> Tuple[float, float]:
        # Calculates the distances to the two nearest rows of flags.
        distances = sorted([self.red_distance, self.yellow_distance,
                            self.green_distance, self.blue_distance])
        
        return distances[0], distances[1]

    def get_distance_from_origin(self) -> float:
        # Calculates the approximate distance from the center of the area.
        x = self.green_distance - self.yellow_distance
        y = self.red_distance - self.blue_distance

        return math.sqrt(x**2 + y**2)

def calculate_average_distance(person: Person, others: List[Person]) -> float:
    # Calculates the average distance of a person from a list of other people.
    if not others:
        return 0.0

    person_origin_distance = person.get_distance_from_origin()
    distances_to_others = [
        abs(person_origin_distance - other.get_distance_from_origin())
        for other in others
    ]
    return mean(distances_to_others)

def find_outliers(people: List[Person], top_percentage: float = 0.1) -> List[Tuple[Person, float]]:
    # Identifies the top percentage of people who are furthest away from others.
    if not people:
        return []

    person_distances: List[Tuple[Person, float]] = []
    for i, person in enumerate(people):
        others = people[:i] + people[i+1:]  # Exclude the current person
        average_distance = calculate_average_distance(person, others)
        person_distances.append((person, average_distance))

    # Sort by average distance in descending order
    person_distances.sort(key=lambda item: item[1], reverse=True)

    num_outliers = int(len(person_distances) * top_percentage)
    return person_distances[:num_outliers]

def generate_sample_people(num_people: int) -> List[Person]:
    # Generates a list of sample people with random distances to flag rows.
    people = []

    for _ in range(num_people):
        # Simulate distances, ensuring they are non-negative
        red = abs(random.gauss(5, 2))
        yellow = abs(random.gauss(5, 2))
        green = abs(random.gauss(5, 2))
        blue = abs(random.gauss(5, 2))
        people.append(Person(red, yellow, green, blue))

    return people

# ---  Main Program --- 
group_of_people = generate_sample_people(100) # Generate a sample group of 100 people

# Find the 10% of people who are furthest away from others
furthest_people = find_outliers(group_of_people, top_percentage=0.1)

print("The 10% of people who are furthest away from others:")
for person, avg_distance in furthest_people:
    print(f"- Person (Distances: Red={person.red_distance:.2f}, Yellow={person.yellow_distance:.2f}, Green={person.green_distance:.2f}, Blue={person.blue_distance:.2f}) => Average distance from others = {avg_distance:.2f}")