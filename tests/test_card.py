from blackjack.card import Card

def test_card_show():
        card = Card("Spades", "1")
        assert card.__str__() == "1 of Spades"