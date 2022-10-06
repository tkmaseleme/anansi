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
                        if self.value == 11:
                                self.value = "Jack"
                        elif self.value == 12:
                                self.value = "Queen"
                        elif self.value == 13:
                                self.value = "King"
                        elif self.value == 1:
                                self.value = "Ace"  
                        return ("{} of {}".format(self.value, self.suit))   
                else:
                        return "Card Completely Invalid"