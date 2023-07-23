# tests/test_blackjack_game.py
from idanansi.blackjack import BlackjackGame
from idanansi.blackjack import Player
from idanansi.blackjack import Hand
from idanansi.card import Card
from idanansi.deck import Deck
    
def test_blackjack_game_setup():
    game = BlackjackGame()
    assert game.player is None
    assert game.dealer is None
    assert game.deck is None
    assert game.minimum_bet == 10


