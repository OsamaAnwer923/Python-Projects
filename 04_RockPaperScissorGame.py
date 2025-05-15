import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock,paper,scissors]
human_choice = int(input('what do you choose? Type 0 for rock, 1 for paper or 2 for scissors'))
human_selection = rock_paper_scissors[human_choice]
print(human_selection)
print('computer choice:')
computer_choice = random.randint(0,2)
computer_selection = rock_paper_scissors[computer_choice]
print(computer_selection)
if human_selection == rock_paper_scissors[0] and computer_selection == rock_paper_scissors[2]:
    print("You won")
elif human_selection == rock_paper_scissors[1] and computer_selection == rock_paper_scissors[0]:
    print("You won")
elif human_selection == rock_paper_scissors[2] and computer_selection == rock_paper_scissors[1]:
    print("You won")
elif human_selection == computer_selection:
    print("it is a tie")
else:
    print("computer won")
