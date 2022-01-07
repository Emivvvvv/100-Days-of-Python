############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
start_again = True
while start_again:
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]

    def draw_card():
        return cards[random.randint(0, 12)]

    def calculate_score(which_deck):
        score = sum(which_deck)
        if score == 21 and len(which_deck) == 2:
            return 0
        elif score > 21 and 11 in which_deck and which_deck == user_cards:
            score -= 10
            user_cards.remove(11)
            user_cards.append(1)
        elif score > 21 and 11 in which_deck and which_deck == computer_cards:
            score -= 10
            computer_cards.remove(11)
            computer_cards.append(1)
        else:
            return score

    def compare(user_score, computer_score):
        if user_score > computer_score :
            return "You win! :)"
        elif user_score == computer_score:
            return "It's a draw! :|"
        else:
            return "You lose. :("

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}. Current score = {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 and computer_score == 0:
        print("It's a draw! You both have blackjack")
    elif user_score == 0 and computer_score != 0:
        print("You win! You have blackjack")
    elif user_score != 0 and computer_score == 0:
        print("Computer wins! Computer has blackjack")

    should_continue = True
    while should_continue:
        draw_another_card = input("Would you like to draw another card? 'y' for yes or 'n' for no.")
        if draw_another_card == 'y':
            user_cards.append(draw_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}. Current score = {user_score}")
            if int(user_score) > 21:
                print("You lose! :(")
                break
        elif draw_another_card == 'n':
            print(f"Your final hand: {user_cards}. Your final score = {user_score}")
            while computer_score < 17:
                computer_cards.append(draw_card())
                computer_score = calculate_score(computer_cards)
            print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
            if int(computer_score) > 21:
                print("You win! :)")
                break
            winner = compare(user_score, computer_score)
            print(winner)
            should_continue = False
    start_again_check = input("Would you like to play again? if yes type 'y' else type 'n'.")
    if start_again_check == 'n':
        start_again = False
    elif start_again_check == 'y':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print("You typed wrong. Program closing.")
        start_again = False