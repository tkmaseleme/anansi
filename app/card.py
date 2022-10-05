class Card:
        def __init__(self, suit, val):
                self.suit = suit
                self.value = val
                       
        def show(self):
                
                if self.suit not in ["Spades", "Clubs", "Diamonds", "Hearts"] and self.value in range(1, 14):
                        return "Card Suit Invalid"
                elif self.suit in ["Spades", "Clubs", "Diamonds", "Hearts"] and self.value not in range(1, 14):
                        return "Card Value Invalid"
                elif self.suit in ["Spades", "Clubs", "Diamonds", "Hearts"] and self.value in range(1, 14):
                        return ("{} of {}".format(self.value, self.suit))   
                else:
                        return "Card Completely Invalid"