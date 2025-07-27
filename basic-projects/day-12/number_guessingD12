import random

game_running = True  

number_of_guesses_h = 5
number_of_guesses_e = 10

def check_guess(users_choice, computers_choice, turns) :
  if users_choice > computers_choice:
    print("Too high")
    return turns - 1
  elif users_choice < computers_choice:
    print("Too low")
    return turns - 1
  else :
    print("You guessed it!")

def choose_difficulty():
  print("Chose a level of difficulty, 'h' for hard 'e'for easy")
  if input() == "h":
    
    return number_of_guesses_h
  else :
    
    return number_of_guesses_e

def game():
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  computers_choice = random.randint(1,100)
  turns = choose_difficulty()
  
  user_choice = 0

  while turns != 0: 
    
    print(f"You have {turns} attempts remaining to guess the number.")
    
    users_choice = int(input("Make a guess: "))

    turns = check_guess(users_choice, computers_choice, turns)
    
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif users_choice != computers_choice:
      print("Guess again.")

game()
  