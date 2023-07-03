class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def clear_cards(self):
        self.cards = []

    def get_hand_value(self):
        value = 0
        num_aces = 0

        for card in self.cards:
            if card.rank in ["King", "Queen", "Jack"]:
                value += 10
            elif card.rank == "Ace":
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value
