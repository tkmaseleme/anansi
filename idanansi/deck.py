#
# The file deck.py
#
# Created On Tue Jul 04 2023
#
# Copyright (c) 2023 Trevor K Maseleme
#


import random
from idanansi.card import Card

# This creates a deck of 52 cards
class Deck:
    def __init__(self):
        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", 
                 "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    