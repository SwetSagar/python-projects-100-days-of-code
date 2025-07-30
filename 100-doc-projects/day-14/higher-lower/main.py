
print("Welcome to the Higher Lower Game!")

import art
import game_data
import random

print(art.logo)

## Compare A code
compare_A = print(f"Compare A: {game_data.data[0]['name']}, a {game_data.data[0]['description']}, from {game_data.data[0]['country']}.")

print(art.vs)

## Compare B code

compare_B = print(f"Against B: {game_data.data[1]['name']}, a {game_data.data[1]['description']}, from {game_data.data[1]['country']}.")

game_running = True
score = 0

while game_running:
    # Randomly select two items from the game data
    compare_A = random.choice(game_data.data)
    compare_B = random.choice(game_data.data)

    # Ensure that A and B are not the same
    while compare_A == compare_B:
        compare_B = random.choice(game_data.data)

    print(art.logo)
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
    print(art.vs)
    print(f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")

    # Ask user for their choice
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Determine the winner
    if (user_choice == 'A' and compare_A['follower_count'] > compare_B['follower_count']) or \
       (user_choice == 'B' and compare_B['follower_count'] > compare_A['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_running = False
        print(f"Sorry, that's wrong. Final score: {score}.")
