import random
from game_data import data

first_number = random.randint(0, 49)
print(first_number)
print(f"{data[first_number]['name']}, {data[first_number]['description']}, from {data[first_number]['country']}")
opt_a_number = random.randint(0,49)
opt_b_number = random.randint(0, 49)
correct = ""
if data[opt_a_number]['follower_count'] > data[opt_b_number]['follower_count']:
  correct = "a"
else:
  correct = "b"
points = 0
player_guess = input("Type 'A' or 'B' ").lower()
if player_guess == correct:
  print("Correct!")
  points = points + 1
else:
  print(f"Wrong. Your final score is {points}")
