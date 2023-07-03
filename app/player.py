import json

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []

        # Create a profile for the player
        self.create_profile()

    def create_profile(self):
        profile = {
            "name": self.name,
            "money": self.money,
            "cards": []
        }

        # Save the profile to a JSON file
        filename = f"profile_{self.name}.json"
        with open(filename, "w") as file:
            json.dump(profile, file)

    def add_card(self, card):
        self.cards.append(card)
