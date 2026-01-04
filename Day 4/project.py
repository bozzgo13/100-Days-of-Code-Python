# Rock Paper Scissors
# player selects 0 for rock, 1 for paper and 2 for scissors
# computer also selects its option using random function


# I am using Text to ASCII art from https://patorjk.com/software/taag
# and rock, paper, scissors ASCII art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
import random

def print_rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
def print_paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

def print_scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def print_win():
    print("""
 █████ █████                                         ███             ███
▒▒███ ▒▒███                                         ▒▒▒             ▒███
 ▒▒███ ███    ██████  █████ ████    █████ ███ █████ ████  ████████  ▒███
  ▒▒█████    ███▒▒███▒▒███ ▒███    ▒▒███ ▒███▒▒███ ▒▒███ ▒▒███▒▒███ ▒███
   ▒▒███    ▒███ ▒███ ▒███ ▒███     ▒███ ▒███ ▒███  ▒███  ▒███ ▒███ ▒███
    ▒███    ▒███ ▒███ ▒███ ▒███     ▒▒███████████   ▒███  ▒███ ▒███ ▒▒▒ 
    █████   ▒▒██████  ▒▒████████     ▒▒████▒████    █████ ████ █████ ███
   ▒▒▒▒▒     ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒       ▒▒▒▒ ▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒ ▒▒▒ 
    """)
def print_lose():
    print("""
 █████ █████                        ████                            ███
▒▒███ ▒▒███                        ▒▒███                           ▒███
 ▒▒███ ███    ██████  █████ ████    ▒███   ██████   █████   ██████ ▒███
  ▒▒█████    ███▒▒███▒▒███ ▒███     ▒███  ███▒▒███ ███▒▒   ███▒▒███▒███
   ▒▒███    ▒███ ▒███ ▒███ ▒███     ▒███ ▒███ ▒███▒▒█████ ▒███████ ▒███
    ▒███    ▒███ ▒███ ▒███ ▒███     ▒███ ▒███ ▒███ ▒▒▒▒███▒███▒▒▒  ▒▒▒ 
    █████   ▒▒██████  ▒▒████████    █████▒▒██████  ██████ ▒▒██████  ███
   ▒▒▒▒▒     ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒ 
    """)

def print_tie():
    print("""
 █████  █████     ██                          █████     ███           ███
▒▒███  ▒▒███     ███                         ▒▒███     ▒▒▒           ▒███
 ▒███  ███████  ▒▒▒   █████      ██████      ███████   ████   ██████ ▒███
 ▒███ ▒▒▒███▒        ███▒▒      ▒▒▒▒▒███    ▒▒▒███▒   ▒▒███  ███▒▒███▒███
 ▒███   ▒███        ▒▒█████      ███████      ▒███     ▒███ ▒███████ ▒███
 ▒███   ▒███ ███     ▒▒▒▒███    ███▒▒███      ▒███ ███ ▒███ ▒███▒▒▒  ▒▒▒ 
 █████  ▒▒█████      ██████    ▒▒████████     ▒▒█████  █████▒▒██████  ███
▒▒▒▒▒    ▒▒▒▒▒      ▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒       ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒ 
    """)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
computer = random.randint(0,2);

print("\nYou chose")
if choice == 0:
    print_rock()
elif choice == 1:
    print_paper()
else:
    print_scissors()

print("Computer chose")
if computer == 0:
    print_rock()
elif computer == 1:
    print_paper()
else:
    print_scissors()

if computer == choice:
    print_tie()
elif choice == 0 and computer == 1: # rock vs paper
    print_lose()
elif choice == 0 and computer == 2: # rock vs scissors
    print_win()
elif choice == 1 and computer == 0: # paper vs rock
    print_win()
elif choice == 1 and computer == 2: # paper vs scissors
    print_lose()
elif choice == 2 and computer == 0: # scissors vs rock
    print_lose()
elif choice == 2 and computer == 1: # scissors vs paper
    print_win()
