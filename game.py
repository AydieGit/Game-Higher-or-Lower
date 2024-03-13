import art
from game_data import data
import random

compare_a_number = random.randint(0,49)
compare_b_number = random.randint(0,49)
def picking_random():
  compare_a_number = random.randint(0,49)
  compare_b_number = random.randint(0,49)
  print(art.logo)
  print(f"Compare A: {data[compare_a_number]['name']}, a {data[compare_a_number]['description']}, from {data[compare_a_number]['country']}")
  print(art.vs)
  print(f"Against B: {data[compare_b_number]['name']}, a {data[compare_b_number]['description']}, from {data[compare_b_number]['country']}")

  a_follower_count = int(data[compare_a_number]['follower_count'])
  b_follower_count = int(data[compare_b_number]['follower_count'])
  return a_follower_count, b_follower_count
#print(f"Compare A: {data[compare_a_number]["name"]["description"]["country"]}")
def game():
  score = 0
  game_status = True
  while game_status:
    a_follower_count, b_follower_count = picking_random()    
    
    user_type = input("Who has more followers? Type 'A' or 'B': ")
    if user_type == "A":
      user_type = a_follower_count
    elif user_type == "B":
      user_type = b_follower_count
    
    if user_type > b_follower_count:
      score += 1
      print(f"You're right! Current score {score}")
    elif user_type > a_follower_count:
      score += 1
      print(f"You're right! Current score {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_status = False

game()


