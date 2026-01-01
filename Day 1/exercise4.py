# Using what you have learnt about the len() function and the input() function. Try to print out the number of
# characters in the user input. Write everything in just 1 line of code.
#
# Split everything into variables.
# Split each step in the previous exercise into a separate variable. One variable called username and one called
# length. Use the variable username in the len calculation.


#single line solution
print(len(input("What is your name?")))

# split everything into variables
print("What is your name?")
username = input()
length = len(username)
print(length)


