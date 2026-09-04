import random
import art


def compare(u_score,c_score):
    """compares the score of computer and user"""
    if u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Computer went over. You win 😁"
    elif u_score == c_score:
        return "Draw 🙃"
    elif u_score > c_score:
        return "You win 😃"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif c_score == 0:
        return"Lose, opponent has Blackjack 😱"
    else :
        return "You lose 😤"
def deal():
    """deals a card"""
    og_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(og_cards)
    return card

def score_count(cards):
    """calculates points as per the rules"""
    if sum(cards) == 21 and len(cards) == 2:
        print("if1")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)

def play_game():
    print(art.logo)
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1
    end_game = False
    for _ in range(2):
        user_cards.append(deal())
        comp_cards.append(deal())

    while not end_game:
        user_score = score_count(user_cards)
        comp_score = score_count(comp_cards)
        print(f"Your cards : {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            end_game = True
        else:
            p_ass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if p_ass == "y":
                user_cards.append(deal())
                print("exe")
            else:
                end_game = True
        while comp_score != 0 and comp_score < 17:
            comp_cards.append(deal())
            comp_score = score_count(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, computer's score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    play_game()
