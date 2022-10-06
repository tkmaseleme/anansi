class Player:
        def __init__(self, name, chips):
                self.name       = name
                self.hand       = []
                self.chips      = chips
                
        def draw(self, deck):
                self.hand.append(deck.drawCard())
                return self
        
        def showHand(self):
                for card in self.hand:
                        print(card.show())