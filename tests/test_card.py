import app

def test_card_show():
        card = app.Card("Spades", 1)
        assert card.show() == "1 of Spades"
        
def test_card_wrong_suit():
        card = app.Card("Quilt", 2)
        assert card.show() == "Card Suit Invalid"
        
def test_card_wrong_value():
        card = app.Card("Spades", 14)
        assert card.show() == "Card Value Invalid"
        
def test_card_xard_invalid():
        card = app.Card("Quilt", 15)
        assert card.show() == "Card Completely Invalid" 