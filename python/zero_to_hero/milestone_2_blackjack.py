# IN PROGRESS

import random

suits = ("Hearts", "Clubs", "Spades", "Diamonds")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, 
          "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

active_game = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"    

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        return f"{self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_cards = []
        for _ in range(2):
            dealt_cards.append(self.deck.pop())
        return dealt_cards

test_deck = Deck()
test_deck.shuffle()

my_hand = test_deck.deal()
for card in my_hand:
    print(card)
print(len(test_deck.deck))

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        pass

    def adjust_for_ace(self):
        pass

  class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        if self.bet <= self.total:
            self.total -= self.bet
        else:
            raise InsufficientChipsError
