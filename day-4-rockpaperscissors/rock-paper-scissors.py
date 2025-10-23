import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
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

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
choices = [rock, scissors, paper]

print(choices[human_choice])
print("Computer chose:")
print(choices[computer_choice])

if human_choice == computer_choice:
    print("Draw")
else:
    #if human_choice < computer_choice and human_choice - computer_choice == -1 or human_choice > computer_choice and human_choice - computer_choice != 1:
    if human_choice == 0 and computer_choice == 1 or human_choice == 1 and computer_choice == 2 or human_choice == 2 and computer_choice == 0:
        print("Human Wins")
    #elif computer_choice < human_choice and computer_choice - human_choice == -1 or computer_choice > human_choice and computer_choice - human_choice != 1:
    else:
        print("Computer Wins")