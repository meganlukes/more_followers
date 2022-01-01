import random
from game_data import data

first_number = random.randint(0, 49)
name = data[first_number]['name']

print(first_number)
print(name)