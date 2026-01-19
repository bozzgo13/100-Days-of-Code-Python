import random
import art
import game_data

current_score = 0
correct_answer = True
opponent_a = random.choice(game_data.data)

while correct_answer:
    # Clear the screen
    print("\n"*20)
    print(art.logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")

    opponent_b = random.choice(game_data.data)

    print(f"Compare A: {opponent_a["name"]}, a {opponent_a["description"]}, from {opponent_a['country']}")
    print(art.vs)
    print(f"Against B: {opponent_b["name"]}, a {opponent_b["description"]}, from {opponent_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A' and opponent_a['follower_count'] > opponent_b['follower_count']:
        correct_answer = True
        current_score += 1
    elif choice == 'B' and opponent_a['follower_count'] < opponent_b['follower_count']:
        correct_answer = True
        current_score += 1
        opponent_a = opponent_b # Making account at position B become the next account at position A.
    else:
        correct_answer = False
# Clear the screen
print("\n"*20)
print(art.logo)
print(f"Sorry, that's wrong. Final score: {current_score}.")
