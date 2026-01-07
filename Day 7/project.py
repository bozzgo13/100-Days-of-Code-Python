import random
words=["abeceda", "sreča", "jabolko", "sladoled", "morje", "veselje", "avto", "sonce", "hiša", "mama", "ata", "traktor"]
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

random_word=random.choice(words)

game_over = False
number_of_wrong_guesses = 0
max_number_of_wrong_guesses = 6
correct_letters=[]
print("Ugotovi besedo:")
masked_word = ""
for letter in random_word:
    masked_word += "_"
print(masked_word)


while not game_over:
    user_letter = input("Vpiši črko: ").lower()

    masked_word = ""
    for letter in random_word:
        if user_letter == letter:
            correct_letters.append(user_letter)
            masked_word += user_letter
        elif letter in correct_letters:
            masked_word += letter
        else:
            masked_word += "_"

    if user_letter not in random_word:
        number_of_wrong_guesses += 1
        print("Črke ni v besedi!")
    else:
        print("Našel si črko!")

    print(masked_word)
    print(HANGMAN[number_of_wrong_guesses])

    print(f"***** Preostalih življenj: {max_number_of_wrong_guesses-number_of_wrong_guesses}/{max_number_of_wrong_guesses} *****")

    if max_number_of_wrong_guesses == number_of_wrong_guesses:
        print("Izgubil si")
        game_over = True

    if "_" not in masked_word:
        print("Zmagal si")
        game_over = True


print("Konec igre")