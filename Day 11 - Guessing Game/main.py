import random

print("Welcome to the Guess Game")


option=input("Choose a dificulty(easy or hard):")

print("The goal of the game is to guess the number that I am thinking of. It is between 0 and 100")

computer_number=random.randint(0,100)

if option=='easy':
    tries=10
    winning_condition=False
    while tries>0:
        player_number=int(input('Guess a number:'))
        if player_number==computer_number:
            print('You found the number that I was thinking of!')
            winning_condition=True
            break
        elif player_number>computer_number:
            print("The number that I am thinking of is smaller!")
        else:
            print("The number that I am thinking of is bigger!")

    if winning_condition==False:
        print("Better luck next time!")

elif option=='hard':
    tries = 5
    winning_condition = False
    while tries > 0:
        player_number = int(input('Guess a number:'))
        if player_number == computer_number:
            print('You found the number that I was thinking of!')
            winning_condition = True
            break
        elif player_number > computer_number:
            print("The number that I am thinking of is smaller!")
        else:
            print("The number that I am thinking of is bigger!")

    if winning_condition == False:
        print("Better luck next time!")