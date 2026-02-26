import pandas

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
result = [phonetic_dict[letter] for letter in word.upper()]
print(result)

# Result
# Enter a word: Bostjan
# ['Bravo', 'Oscar', 'Sierra', 'Tango', 'Juliet', 'Alfa', 'November']