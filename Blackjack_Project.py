import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score,user_cards, computer_cards):
    user_five_card = len(user_cards) == 5 and user_score <= 21
    computer_five_card = len(computer_cards) == 5 and computer_score <= 21
    
    if user_five_card and not computer_five_card:
        return "You win with a 5-card trick!"
    elif computer_five_card and not user_five_card:
        return "You lose, opponent has a 5-card trick!"
    elif user_five_card and computer_five_card:
        return "It's a draw with both having 5-card tricks!"
    
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card()) # Append the dealt card to the user's hand 1 by 1
        #if using user_cards += [deal_card()], it will append the list instead of the value
        
        computer_cards.append(deal_card())

    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            while not is_game_over:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    print(f"   Your cards: {user_cards}, current score: {user_score}")
                    print(f"   Computer's first card: {computer_cards[0]}")
                    if user_score <= 21 and len(user_cards) ==5:
                        is_game_over = True
                    
                else:
                    is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score,user_cards, computer_cards))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)  # Clear the console
    play_blackjack()
    