from deck import Deck
from player import Player

# Example usage
deck = Deck()
deck.shuffle()

player1 = Player("John", 5000)
player1.draw_cards(deck, 5)

player2 = Player("Jane", 3000)
player2.draw_cards(deck, 5)

player1.save_profile()
player2.save_profile()