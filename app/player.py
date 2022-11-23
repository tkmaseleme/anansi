import json

class Player:
        def __init__(self, name, chips):
                self.name       = name
                self.hand       = []
                self.chips      = chips
            
        def draw(self, deck):
                # print(list(self.hand))
                self.hand.append(deck.drawCard())
                return self
        
        def showHand(self):
                for card in self.hand:
                        print(card.show())
                        
        def player_profile(self):
                profile = {
                        "Name": (self.name).title(),
                        "Balance": self.chips,
                        "Cards": repr(self.hand)
                }
                
                with open(self.name + ".json", "w") as playout:
                        json.dump(profile, playout)