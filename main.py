import random
from game_data import data

first_number = random.randint(0, 49)
print(first_number)
print(f"{data[first_number]['name']}, {data[first_number]['description']}, from {data[first_number]['country']}")
