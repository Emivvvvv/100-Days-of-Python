import random
import art
import game_data

def start_the_game():
    print(art.logo)
    first = {}
    second = {}
    score = 0
    while first == second:
        first = game_data.data[random.randint(0,49)]
        second = game_data.data[random.randint(0,49)]
    return first, second, score

def new_data(winner, loser):
    loser = game_data.data[random.randint(0, 49)]
    while winner == loser:
        loser = game_data.data[random.randint(0, 49)]
    return winner, loser

def vs(first, second, guess, score):
    if first["follower_count"] > second["follower_count"] and guess == "A" or first["follower_count"] < second["follower_count"] and guess == "B":
        score += 1
        print(f"You're right! Current score: {score}.")
        if guess == "A":
            first, second = new_data(first, second)
            return first, second, score
        else:
            first, second = new_data(second, first)
            return first, second, score
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        exit()

def higher_lower_game():
    first, second, score = start_the_game()
    should_continue = True
    while should_continue:
        print(f'Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}')
        print(art.vs)
        print(f'Against B: {second["name"]}, a {second["description"]}, from {second["country"]}')
        while True:
            guess = input("(A/B): ")
            if guess == "a" or guess == "b" or guess == "A" or guess == "B":
                first, second, score = vs(first, second, guess, score)
                break
            else:
                print("You typed unknown key. Please type again.")

higher_lower_game()