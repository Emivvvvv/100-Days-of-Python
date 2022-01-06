import random
rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)
print(f"{rps[user_input]}\n\nComputer chose:\n{rps[computer]}")
if user_input == computer:
    print("DRAW!")
if computer > user_input:
    if user_input == 0 and computer == 2:
        print("You win :)")
    print("You lose :(")
else:
    if user_input == 2 and computer == 0:
        print("You lose :(")
    print("You win :)")


