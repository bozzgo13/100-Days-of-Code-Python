
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()

    for name in names:
        name  = name.strip()#replace(old="\n", new="")
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)