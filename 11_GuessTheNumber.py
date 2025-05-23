import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number = random.randint(1,100)
difficulty_level=input("choose Difficulty level: Tyes'easy' or 'hard':").lower()
if difficulty_level == 'hard':
    attempts=5
else:
    attempts=10
repeat = True
while repeat == True:
    print(f'you have {attempts} remaining to guess the number')
    guess_number=int(input("Make a guess:"))
    attempts-=1
    if guess_number>number:
        print("Too High")
    elif guess_number<number:
        print("Too Low")
    elif guess_number==number:
        print(f"You got it! The answer was {number}.")
        repeat=False
    if attempts==0:
        print(f"You are out of guesses.The answer was{number}")
        repeat=False
