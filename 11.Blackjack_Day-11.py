import random


def select():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw...."
    elif user_score == 0:
        return "You Win with a BLACKJACK..."
    elif user_score == 0:
        return "You lose, Opponent has a BLACKJACK.."
    elif user_score > 21:
        return "You Lose, you went overboard.."
    elif computer_score > 21:
        return "You win, Oppenent went overboard..."
    elif user_score > computer_score:
        return "You Win ..."
    else:
        return "You Lose.."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(select())
        computer_cards.append(select())
    while not is_game_over:
        user_score = calculate_sum(user_cards)
        computer_score = calculate_sum(computer_cards)

        print(f"Your cards are : {user_cards}, Current Score : {user_score}")
        print(f"Computer's first card is : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            game = input(
                "Type 'y' to get another card, or 'n' to pass : ").lower()
            if game == 'y':
                user_cards.append(select())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(select())
        computer_score = calculate_sum(computer_cards)
    print(f"Your cards are : {user_cards}, Current Score : {user_score}")
    print(
        f"Computer's cards are : {computer_cards}, final Score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack (y/n) : ").lower() == 'y':
    play_game()
