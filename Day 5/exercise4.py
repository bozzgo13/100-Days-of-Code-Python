# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# These are the rules of the FizzBuzz game:
#  - Your program should print each number from 1 to 100 in turn and include number 100.
#  - But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#  - When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#  - And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# something extra. I counted how many times it prints numbers, 'Fizz' word, 'Buzz' word and 'FizzBuzz' word
counter = [0, 0, 0, 0]
for num in range(1, 101):
    str = ""
    if num % 3 == 0:
        str += "Fizz"
    if num % 5 == 0:
        str += "Buzz"
    if str == "":
        counter[0] += 1
        str = num
    elif str == "Fizz":
        counter[1] += 1
    elif str == "Buzz":
        counter[2] += 1
    elif str == "FizzBuzz":
        counter[3] += 1
    if num > 1:
        print(", ", end="")
    print(f"({num}): {str}", end="")
print("\n")
print(f"Numbers were printed {counter[0]} times")
print(f"Fizz was printed {counter[1]} times")
print(f"Buzz was printed {counter[2]} times")
print(f"FizzBuzz was printed {counter[3]} times")
