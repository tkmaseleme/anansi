#!/usr/bin/env python3
from card import Card
from deck import Deck
from player import Player


deck = Deck()
deck.shuffle()

amira = Player("Amira", 1000)
for x in range(1,6):
        amira.draw(deck)
        
print("Amira's cards are: ")
amira.showHand()

# test = Card("Spades", 1)
# print(test.show())