import random

class Deck:
    def __init__(self):
        self.deck=[]

    def add_cards(self,new_cards):
        self.deck=new_cards

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        drawn_card=self.deck[0]
        self.deck.pop(0)
        return drawn_card