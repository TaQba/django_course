#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle


# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# RANKS = 'J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    deck = []

    def __init__(self):
        print("Creating Deck")
        self.deck = [(s,r) for s in SUITE for r in RANKS]



    def card_force(self, card):
        return self.card_rank[card]

    def shuffle(self):
        print("Shuffle deck")
        shuffle(self.deck)

    def split(self):
        print("Split deck")
        length = len(self.deck)

        middle_index = length // 2

        first_half = self.deck[:middle_index]
        second_half = self.deck[middle_index:]

        return (first_half, second_half)

    def __str__(self):
        print('This is a desk of cards: ' + str(self.deck))



class Hand:

    def __init__(self, cards):
        self.cards = cards

    def add_card(self, cards):
        self.cards.extend(cards)

    def remove_card(self):
        return self.cards.pop()



class Player(Hand):

    def __init__(self, name, cards):
        self.name = name
        self.hand = Hand(cards)


    def has_cards(self):
        return len(self.hand.cards) != 0

    def play(self):
        drawn_card = self.hand.remove_card()
        print("{} has place: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())

            return war_cards

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

d = Deck()
d.shuffle()

half1, half2 = d.split()


p1 = Player('Zofia', half1)
# name = input("What is you name? ")
p2 = Player('Jakub', half2)

rounds = 0
war_count = 0
while p1.has_cards() and p2.has_cards():
    rounds = rounds + 1
    print("{} has the count {}" .format(p1.name, str(len(p1.hand.cards))))
    print("{} has the count {}".format(p2.name, str(len(p2.hand.cards))))
    print("Play card")

    table_cards = []
    p1_card = p1.play()
    p2_card = p2.play()
    table_cards.append(p1_card)
    table_cards.append(p2_card)

    "WAR"

    if p1_card[1] == p2_card[1]:
        war_count += 1
        table_cards.extend(p1.remove_war_cards())
        table_cards.extend(p2.remove_war_cards())

        if RANKS.index(p1_card[1]) < RANKS.index(p2_card[1]):
            p2.hand.add_card(table_cards)
        else:
            p1.hand.add_card(table_cards)
    else:
        if RANKS.index(p1_card[1]) < RANKS.index(p2_card[1]):
            p2.hand.add_card(table_cards)
        else:
            p1.hand.add_card(table_cards)


print("\nGame has total rounds: {}".format(str(rounds)))
print("with number of wars: {}".format(str(war_count)))

if p1.has_cards() != False:
    winner = p2.name

if p2.has_cards() != False:
    winner = p1.name

print("{} is a winner!".format(winner))