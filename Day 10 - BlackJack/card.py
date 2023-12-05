import deck


card_values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
             'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

suits =['Clubs','Spades','Hearts','Diamonds']
numbers=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']


def make_all_cards():
    all_cards=[]
    for suit in suits:
        for number in numbers:
            new_card=make_card(suit,number)
            all_cards.append(new_card)

    return all_cards

def make_card(suit,number):
    new_card=Card(suit,number)
    return new_card

class Card:
    def __init__(self,suit,number):
        self.suit=suit
        self.number=number
        self.value=card_values[number]




