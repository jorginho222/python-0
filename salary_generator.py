import csv
import random


def generate_salary_by_experience(years_experience):
    base_salary = 200 * years_experience + 2000
    return base_salary + random.randint(1, 199)


def entry_generator(num_rows = 100):
    i = 0

    while i < num_rows:
        years_of_experience = random.randint(1, 10)

        yield years_of_experience, generate_salary_by_experience(years_of_experience)
        i += 1


def generate_csv_data(num_rows = 100):
    header = 'years_of_experience', 'salary'
    data = list(entry_generator(num_rows))

    return [header] + data


def write_csv(filename, data):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return rows

