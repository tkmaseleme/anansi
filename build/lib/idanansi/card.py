#
# The file card.py
#
# Created On Tue Jul 04 2023
#
# Copyright (c) 2023 Trevor K Maseleme
#

# Class to create a standard card with a rank and suit
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"