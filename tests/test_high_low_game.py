from idanansi.card import Card
from idanansi.high_low import HighLow

def test_high_low_setup():
    high_low_game = HighLow()
    assert high_low_game.deck is not None

def test_high_low_compare_cards():
    high_low_game = HighLow()

    # Test cards with equal rank
    card1 = Card("Hearts", "2")
    card2 = Card("Spades", "2")
    result = high_low_game.compare_cards(card1, card2)
    assert result == "equal"

    # Test higher card
    card1 = Card("Hearts", "9")
    card2 = Card("Spades", "4")
    result = high_low_game.compare_cards(card1, card2)
    assert result == "l"

    # Test lower card
    card1 = Card("Hearts", "5")
    card2 = Card("Spades", "10")
    result = high_low_game.compare_cards(card1, card2)
    assert result == "h"

def test_high_low_play(monkeypatch):
    # Mock user input for testing
    user_input = iter(["exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    high_low_game = HighLow()
    high_low_game.play()
    assert high_low_game.deck is not None
