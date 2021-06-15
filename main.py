import art, game_data, random
from replit import clear

def generate_personality(data):
  random_num = random.randint(0, len(data) - 1)
  return data[random_num]

def decide_winner(personality_a, personality_b):
  global winner
  if personality_a['follower_count'] > personality_b['follower_count']:
    winner = personality_a
  else:
    winner = personality_b

def check_winner(user_answer, personality_a, personality_b):
  check = ""
  if personality_a['follower_count'] > personality_b['follower_count']:
    check = 'a'
  else:
    check = 'b'
  if user_answer == check:
    return 1
  else:
    return 0

def output_comparisons(personality_a, personality_b):
  print(f"Compare A: {personality_a['name']}, a {personality_a['description']}, from {personality_a['country']}")
  print(art.vs)
  print(f"Against B: {personality_b['name']}, a {personality_b['description']}, from {personality_b['country']}")


print(art.logo)
data = game_data.data
personality_a = generate_personality(data)

score = 0
end_of_game = False
while not end_of_game:
  winner = ""
  personality_b = generate_personality(data)
  
  decide_winner(personality_a, personality_b)

  output_comparisons(personality_a, personality_b)  

  user_choice = input("Who has more followers? Type 'A' or 'B'. ").lower()

  return_value = check_winner(user_choice, personality_a, personality_b)

  if return_value == 0:
    end_of_game = True
    clear()
    print(f"Wrong! Your final score: {score}")
  else:
    personality_a = winner
    score += 1
    clear()
    print(f"That's correct! Your score: {score}")
