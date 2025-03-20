from datetime import date
from random import randint
import datetime

def calculate_average_age_months(years, months):
    # Calculates the total average age in months.
    return years * 12 + months

def is_leap(year):
    # Checks if a year is a leap year.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_random_birth_date(base_year, age_range_years):
    # Generates a random birth date within a given age range
    start_year = base_year - age_range_years
    end_year = base_year
    year = randint(start_year, end_year)
    month = randint(1, 12)
    max_days = 29 if month == 2 and is_leap(year) else 28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31
    day = randint(1, max_days)

    return datetime.date(year, month, day)

def get_age_in_months(birth_date):
    # Calculates the age in months from a birth date.
    today = date.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_months = age_years * 12 + (today.month - birth_date.month)

    return age_months

def count_students_outside_age_range(classes_data, average_age_months):
    # Counts the total number of students in each class whose age is significantly
    results = {}
    age_threshold = 6  # months

    for class_name, student_birth_dates in classes_data.items():
        older_count = 0
        younger_count = 0

        for birth_date in student_birth_dates:
            student_age_months = get_age_in_months(birth_date)

            if student_age_months > average_age_months + age_threshold:
                older_count += 1
            elif student_age_months < average_age_months - age_threshold:
                younger_count += 1

        results[class_name] = {"older": older_count, "younger": younger_count}

    return results

# ---  Main Program --- 
average_age_years = 20
average_age_months_part = 8
average_age_total_months = calculate_average_age_months(average_age_years, average_age_months_part)

classes_data_realistic = {}
class_sizes = {
    "Class 4": 40,
    "Class 5": 35, 
    "Class 6": 45, 
    "Class 10": 30
}

base_year = date.today().year - average_age_years
age_range = 2 # Assume a reasonable age range around the average

for class_name, size in class_sizes.items():
    classes_data_realistic[class_name] = [generate_random_birth_date(base_year, age_range) for _ in range(size)]

results_realistic = count_students_outside_age_range(classes_data_realistic, average_age_total_months)
print("Results for Realistic Data:\n")

for class_name, counts in results_realistic.items():
    print(f"{class_name}:\n Older than avg +6 months: {counts['older']}\n Younger than avg -6 months: {counts['younger']}\n")