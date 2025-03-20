from datetime import date
from typing import List, Tuple
from statistics import mean
from random import randint
import json

class Person:
    # Represents a person with a name and birth date.
    def __init__(self, name: str, birth_date: date):
        self.name = name
        self.birth_date = birth_date

    def get_age(self) -> int:
        # Calculates the age of the person in years.
        today = date.today()
        birth_year = self.birth_date.year
        birth_month = self.birth_date.month
        birth_day = self.birth_date.day
        age = today.year - birth_year

        # Check if the birth date has occurred this year
        if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
            age -= 1  # Subtract 1 if the birth date hasn't passed yet
            
        return age
    
    def to_dict(self):
        # Returns a dictionary representation of the Person object.
        return {
            "name": self.name,
            "birth_date": self.birth_date.isoformat()  # Convert date to string format
        }

def calculate_age_difference(person: Person, 
                             others: List[Person]) -> float:
    # Calculates the average age difference of a person from a list of other people.
    if not others:
        return 0.0

    person_age = person.get_age()
    age_differences = [abs(person_age - other.get_age()) for other in others]

    return mean(age_differences)

def find_outliers(people: List[Person], 
                  top_percentage: float = 0.2
                  ) -> List[Tuple[Person, float]]:
    # Identifies the top percentage of people with the largest average age difference.
    if not people:
        return []

    person_differences: List[Tuple[Person, float]] = []
    for i, person in enumerate(people):
        others = people[:i] + people[i+1:]  # Exclude the current person
        average_difference = calculate_age_difference(person, others)
        person_differences.append((person, average_difference))

    # Sort by average age difference in descending order
    person_differences.sort(key=lambda item: item[1], reverse=True)

    num_outliers = int(len(person_differences) * top_percentage)
    return person_differences[:num_outliers]

def generate_sample_people(num_people: int) -> List[Person]:
    # Generates a list of sample people with random birth dates.
    people = []

    for i in range(num_people):
        # Simulate birth years between 1950 and 2020
        birth_year = randint(1950, 2020)
        # Keep it simple for months and days
        birth_month = randint(1, 12)
        birth_day = randint(1, 28)

        try:
            birth_date_obj = date(birth_year, birth_month, birth_day)
            people.append(Person(f"Person {i+1}", birth_date_obj))
        except ValueError:
            # Handle cases where the generated date is invalid (e.g., Feb 30)
            pass

    return people

# ---  Main Program --- 
population = generate_sample_people(100) # Generate a sample population of 100 people
# print('\nData:', json.dumps([p.to_dict() for p in population]))

# Find the 20% of people with the largest age difference
outliers = find_outliers(population, top_percentage=0.2)

print("\nTop 20% of people with the largest age difference from others:")
for person, avg_difference in outliers:
    print(f"- {person.name}: Average age difference = {avg_difference:.2f} years")