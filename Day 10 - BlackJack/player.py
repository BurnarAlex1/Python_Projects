class Player:
    def __init__(self,money):
        self.money=int(money)
        self.cards=[]

    def add_card(self,card):
        self.cards.append(card)

    def show_cards(self):
        for card in self.cards:
            print(card.number + ' of '+ card.suit)

    def throw_cards(self):
        self.cards=[]



    def get_card_values(self):
        value=0
        for card in self.cards:
            value=value+card.value

        return value
