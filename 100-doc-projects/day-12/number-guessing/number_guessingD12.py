print("Welcome to the Number Guessing Game!")
import art
import random
print(art.logo)


number_to_guess = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

game_running = True

## choose difficulty

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    print('You have 10 attempts to guess the number.')
    attempts = 10
elif difficulty == "hard":
    print('You have 5 attempts to guess the number.')
    attempts = 5
else:
    print("Invalid difficulty. Defaulting to 'easy'.")
    attempts = 10

while game_running:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please guess a number between 1 and 100.")
        continue

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number {number_to_guess}.")
        game_running = False
    elif guess < number_to_guess:
        print("Too low.")
        attempts -= 1
        continue
    else:
        print("Too high.")
        attempts -= 1
        continue

    attempts -= 1

    if attempts == 0:
        print(f"You've run out of attempts. The number was {number_to_guess}.")
        game_running = False
            

    
