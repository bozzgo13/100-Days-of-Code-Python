import random
print ("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 10

if difficulty == "hard":
    attempts = 5

guessed = False
while attempts > 0 and guessed == False:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == random_number:
        guessed = True
    else:
        if guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        if attempts > 0:
            print("Guess again.")

if guessed == True:
    print(f"Congratulations! You guessed the number {random_number}!")
else :
    print(f"Sorry, you did not guess the number {random_number}.")