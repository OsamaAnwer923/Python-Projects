import random
cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = random.choices(cards,k=2)
computer_cards = random.choices(cards,k=2)

def score(list1):
    score = sum(list1)
    while 11 in list1 and score > 21:
        list1[list1.index(11)] = 1
        score = sum(list1)
    return score



if 11 in computer_cards and 10 in computer_cards:
    print(f"Your cards: {user_cards}, current score:{score(user_cards)}")
    print("You Lose. BlackJack")
elif 11 in user_cards and 10 in user_cards:
    print(f"Your cards: {user_cards}, current score:{score(user_cards)}")
    print( "User Won. . BlackJack")
else:

    game=False
    while game == False:
        print(f"Your cards: {user_cards}, current score:{score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]} ")
        another_card = input("if you want to get another card type 'yes' and if not press'no' ").lower()
        if another_card == 'yes':
            user_cards.append(cards[random.randint(0,len(cards)-1)])
        elif another_card == 'no':
            while score(computer_cards)<17:
                computer_cards.append(cards[random.randint(0,len(cards)-1)])
        if score(user_cards)>21:
            print("You Lose. Score is greater than 21")
            game = True
        else:
            if score(computer_cards)<score(user_cards):
                print("You Won")
                game = True
            elif score(computer_cards)>score(user_cards):
                print("Computer Won")
                game = True
            else:
                print("It is draw")
                game = True
            print(f"Your Final Hand: {user_cards} and Final score: {score(user_cards)}")
            print(f"Computer Final Hand: {computer_cards} and computer score: {score(computer_cards)}")