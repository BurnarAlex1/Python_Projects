import AuctionPlayer

print('Welcome to the silent auction application!')


check=True
players_list=[]
while check==True:
    name=input("Give the player's name: ")
    bid=input("Give the player's bid: ")
    player=AuctionPlayer.AuctionPlayer(name,bid)
    players_list.append(player)

    option= input("Do you want to add another player?(Y/N)")

    if option=='N':
        check=False

max=0
winning_player="Nobody"
for player in players_list:
    if player.bid>max:
        max=player.bid
        winning_player=player.name

print('The player that won the bid is '+ winning_player +' with a bid of '+ str(max)+'$')
