from art import logo
import random

print(logo)

def remaining_life():
    global life
    life -= 1
    if life == 0:
        print("You've run out of guesses, you lose.")
        exit()
    print(f"You have {life} attempts remaining to guess the number.")

should_continue = True
while should_continue:
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
        life = 11
        remaining_life()
    elif difficulty == "hard":
        life = 6
        remaining_life()
    else:
        print("You typed unknown difficulty. as punishment, the game has switched to hard mode!")
        life = 6
        remaining_life()
    while True:
        guess = int(input("Make a guess: "))
        if guess > random_number and guess < 101 and guess > 0:
            print("Too high!")
            remaining_life()
        elif guess < random_number and guess < 101 and guess > 0:
            print("Too low!")
            remaining_life()
        elif guess == random_number:
            print(f"Well done! You guessed right. The number that I guessed was {random_number}")
            again = input("Would you like to play again? if yes type 'y' or for no type 'n'")
            if again == "y":
                print("Restarting the game...")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                break
            else:
                print("Goodbye!")
                should_continue = False
                break
        else:
            print("You have typed something under 0 or upper 100. Please type a number just between 1-100.")
