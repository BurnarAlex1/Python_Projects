import card
import deck
import player


new_cards=card.make_all_cards()
new_deck=deck.Deck()

print('Welcome to BlackJack!')
new_player=player.Player(1000)
computer=player.Player(0)
while True:
    if new_player.money==0:
        print("You no longer have money!")
        break
    option=input("Do you want to continue the game?(Y/N)")
    if option=='N':
        break
    new_deck.add_cards(new_cards)
    new_deck.shuffle_deck()
    new_player.throw_cards()
    print("You currently have "+str(new_player.money)+'$')
    bet=int(input("Please give the amount you want to bet: "))
    if bet>new_player.money:
        print('The bet you choose is bigger then the amount of money you have!')
        continue


    while True:
        print('You have the following cards:')
        new_player.show_cards()
        option=input("Do you want to draw a card?(Yes or No) ")

        if option=='No':
            break
        elif option=='Yes':
            drawn_card = new_deck.draw_card()
            new_player.add_card(drawn_card)

        if new_player.get_card_values()>21:
            break

    computer.throw_cards()
    if new_player.get_card_values()>21:
        print("The player has lost because they went over 21!")
        new_player.money=new_player.money-bet
    else:
        while computer.get_card_values()<new_player.get_card_values():
            drawn_card=new_deck.draw_card()
            computer.add_card(drawn_card)

        if computer.get_card_values()<22 and computer.get_card_values()>new_player.get_card_values():
            print("The computer won this match with the following cards:")
            computer.show_cards()
            new_player.money = new_player.money - bet
        elif computer.get_card_values()==new_player.get_card_values():
            print("There was a draw!")
            print("The computer has drawn the following cards:")
            computer.show_cards()
        else:
            print("The player has won this match!")
            print("The computer has drawn the following cards:")
            new_player.money=new_player.money+bet
            computer.show_cards()

print('The game has ended and you got out with '+str(new_player.money)+'$')
