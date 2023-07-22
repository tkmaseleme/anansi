# tests/test_blackjack_game.py
from anansi.blackjack import BlackjackGame
from anansi.blackjack import Player
from anansi.blackjack import Hand
from anansi.card import Card
from anansi.deck import Deck
    
def test_blackjack_game_setup():
    game = BlackjackGame()
    assert game.player is None
    assert game.dealer is None
    assert game.deck is None
    assert game.minimum_bet == 10


