import random
from art import logo
cards=[2,3,4,5,6,7,8,9,10,10,10,10,10,11]
def deal_cards():
    """returns a random card from a list  """
    card= random.choice(cards)
    return card
def calculate_score(card):
    """ take a list of cards and return the score from the cards"""
    if sum(card) >= 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    if computer_score==0:
        return "Loss,opponent has black jack"
    if user_score==0:
        return "Win with a black jack "
    if user_score > 21:
        return "you went over. you loss "
    elif computer_score> 21:
        return "opponent went over.you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you loss"
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    user_score=-1
    computer_score=-1
    is_game_over=False
    for i in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"your cards:{user_card} current score: {user_score}")
        print(f"computer first card:{computer_card[0]}")
        if user_score==0 and computer_score== 0 and user_score>21:
            is_game_over = True
        else:
            user_should_deal=input("type 'y' to add another card or type 'n' to pass : ")
            if user_should_deal=="y":
                user_card.append(deal_cards())
            else:
                is_game_over=True
    while computer_score !=0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score=calculate_score(computer_card)
    print(f"your final hand:{user_card} and final score:{user_score}")
    print(f"your final hand:{computer_card} and final score:{computer_score}")
    print(compare(user_score, computer_score))
while input("do you want to play a game of Blackjack? type 'y' or 'n': ")=="y":
    play_game()

















