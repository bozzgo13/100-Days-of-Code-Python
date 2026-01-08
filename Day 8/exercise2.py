# You are going to write a function called calculate_love_score() that tests the compatibility between two 
# names. To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53
# Example Input 
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

def calculate_love_score(name1, name2):
    upper_name1 = name1.upper()
    upper_name2 = name2.upper()
    
    counter_T = upper_name1.count('T') + upper_name2.count('T')
    counter_R = upper_name1.count('R') + upper_name2.count('R')
    counter_U = upper_name1.count('U') + upper_name2.count('U')
    counter_E = upper_name1.count('E') + upper_name2.count('E')
    
    counter_L = upper_name1.count('L') + upper_name2.count('L')
    counter_O = upper_name1.count('O') + upper_name2.count('O')
    counter_V = upper_name1.count('V') + upper_name2.count('V')

    counter1 = counter_T + counter_R +counter_U + counter_E
    counter2 = counter_L + counter_O +counter_V + counter_E
    
    
    print(counter1 * 10 + counter2)
    
calculate_love_score("Kanye West", "Kim Kardashian") #output : 42