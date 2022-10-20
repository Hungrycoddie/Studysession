import random
import csv

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

full_names = []

for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_names.append(f'{first} {last}')

print(full_names)

path = input('Enter the path to save the file: ')

with open(path, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['First Name', 'Last Name'])
    for name in full_names:
        writer.writerow(name.split(' '))