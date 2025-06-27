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
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.values -= 10
            self.aces -= 1

# # TESTING DEALING CARDS TO PLAYER HAND

# my_hand = Hand()
# my_hand.add_card(test_deck.deal())
# my_hand.add_card(test_deck.deal())

# for card in my_hand.cards:
#     print(card)
# print(my_hand.value)

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet            

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"How many chips would you like to bet? "))
        except ValueError:
            print(f"Input must be a number")
        else:
            if chips.bet > chips.total:
                print(f"Insufficient chips. Your bet cannot exceed {chips.total}.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global active_game

    while True:
        x = input("Would you like to hit or stand? ")
        if x.lower() == "hit":
            hit(deck, hand)
            break
        elif x.lower() == "stand":
            active_game = False
            print("Player's turn has ended. It is now the Dealer's turn.")
            print("------------")
            break
        else:
            print("Try again")
            continue

def show_some(player, dealer):
    print("Player's cards:")
    for card in player.cards:
        print(card)
    print()
    print(f"Player's score: {player.value}")
    print()
    print("Dealer's cards:")
    print("<hidden card>")
    for card in dealer.cards[1:]:
        print(card)
    print("------------")
    
def show_all(player, dealer):
    print("Player's cards:")
    for card in player.cards:
        print(card)
    print()
    print(f"Player's score: {player.value}")
    print()
    print("Dealer's cards:")
    for card in dealer.cards:
        print(card)
    print()
    print(f"Dealer's score: {dealer.value}")
    print()

def player_busts(player, dealer, chips):
    print("Player busts, Player loses")
    chips.lose_bet()        

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts, Player wins!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Player loses")
    chips.lose_bet()

def push(): # TIE GAME
    print("Player and Dealer tie")

game_deck = Deck()
game_deck.shuffle()
players_chips = Chips() # starts with 100

print(f"The Player has {players_chips.total} chips")

while True:
    print("Start of game")
    print()
    players_cards = Hand()
    dealers_cards = Hand()
    
    for _ in range(2):
        players_cards.add_card(game_deck.deal())
        dealers_cards.add_card(game_deck.deal())
    
    take_bet(players_chips)  
    show_some(players_cards, dealers_cards)      
    
    while active_game:
        hit_or_stand(game_deck, players_cards)
        show_some(players_cards, dealers_cards)
        if players_cards.value > 21:
            player_busts(players_cards, dealers_cards, players_chips)
            active_game = False

    if players_cards.value <= 21:
        while dealers_cards.value < 17:
            hit(game_deck, dealers_cards)
            
    show_all(players_cards, dealers_cards)
    
    if dealers_cards.value > 21:
        dealer_busts(players_cards, dealers_cards, players_chips)

    if  21 >= players_cards.value > dealers_cards.value:
        player_wins(players_cards, dealers_cards, players_chips)
    elif players_cards.value < dealers_cards.value <= 21:
        dealer_wins(players_cards, dealers_cards, players_chips)
    elif players_cards.value == dealers_cards.value:
        push(players_cards, dealers_cards, players_chips)
            
    print(f"Player's chip total: {players_chips.total}")
    if players_chips.total == 0:
        print("You are out of chips, thanks for playing")
        break

    play_again = input("Would you like to play again? (Y/N)")
    print("------------")
    if play_again[0].lower() == "y":
        active_game = True
        continue        
    else:
        print("Thanks for playing")
        break
