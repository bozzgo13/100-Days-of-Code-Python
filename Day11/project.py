# All game logic was coded from scratch and developed independently. 
# This implementation was created without consulting the instructor's provided solutions.
# Reference for rules and gameplay flow: https://games.washingtonpost.com/games/blackjack
# No external logic libraries or code snippets were used.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card():
    card = random.choice(cards)
    return card
def get_sum(deck):
    return sum(deck)

player_deck =[]
dealer_deck =[]
game_over = False

card = get_card()
player_deck.append(card)
card = get_card()
dealer_deck.append(card)
card = get_card()
player_deck.append(card)
card = get_card()
dealer_deck.append(card)

print(f"Players deck {player_deck}, SUM: {get_sum(player_deck)}")
print(f"Dealers deck [X, {dealer_deck[1]}]")
player_choice = input("Type H for hit or S for Stand: ").upper()

while player_choice == "H" and game_over == False:
    card = get_card()
    player_deck.append(card)
    print(f"Players deck {player_deck}, SUM: {get_sum(player_deck)}")
    if(get_sum(player_deck) > 21):
        print("Game Over - Bust")
        game_over = True
    else:
        player_choice = input("Type H for hit or S for Stand: ").upper()

if game_over == False:
    print(f"Players deck {player_deck}, SUM: {get_sum(player_deck)}")
    print(f"Dealers deck {dealer_deck}, SUM: {get_sum(dealer_deck)}")

    while get_sum(dealer_deck) <= 16:
        card = get_card()
        dealer_deck.append(card)
        print(f"Dealers deck {dealer_deck}, SUM: {get_sum(dealer_deck)}")

    player_sum = get_sum(player_deck)
    dealer_sum = get_sum(dealer_deck)
    if dealer_sum > 21:
        print("Game Over - Dealer Bust, Player Wins")
    elif player_sum > dealer_sum:
        print("Game Over - Player Wins")
    elif player_sum < dealer_sum:
        print("Game Over - Dealer Wins")
    else:
        print("Game Over - It's a Tie")