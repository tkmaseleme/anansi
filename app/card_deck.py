import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0

        for card in self.cards:
            if card.rank == "Ace":
                value += 11
                num_aces += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                value += 10
            else:
                value += int(card.rank)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def show(self, hide_first_card=False):
        if hide_first_card:
            print("Hidden Card")
            for card in self.cards[1:]:
                print(card)
        else:
            for card in self.cards:
                print(card)

class Player:
    def __init__(self, name, money):
        self.name = name
        self.hand = Hand()
        self.wins = 0
        self.money = money
        self.initial_money = money

    def draw_card(self, deck):
        card = deck.draw_card()
        if card is not None:
            self.hand.add_card(card)

    def show_hand(self, hide_first_card=False):
        print(f"\n{self.name}'s hand:")
        self.hand.show(hide_first_card)

    def win_round(self, bet):
        self.wins += 1
        self.money += bet

class Dealer(Player):
    def draw_card(self, deck, hide_first_card=False):
        card = deck.draw_card()
        if card is not None:
            self.hand.add_card(card)

    def show_hand(self, hide_first_card=False):
        print(f"\n{self.name}'s hand:")
        self.hand.show(hide_first_card)

class BlackjackGame:
    def __init__(self):
        self.player = None
        self.dealer = None

    def setup_game(self):
        self.deck = Deck()
        self.deck.shuffle()

        print("--- Welcome to Blackjack! ---")
        name = input("Enter your name: ")
        money = int(input("Enter the amount of money you want to start with: "))
        self.player = Player(name, money)
        self.dealer = Dealer("Dealer", float("inf"))

    def get_bet(self):
        while True:
            try:
                bet = int(input("\nPlace your bet: $"))
                if bet <= self.player.money:
                    return bet
                else:
                    print("Invalid bet. You don't have enough money.")
            except ValueError:
                print("Invalid bet. Please enter a valid amount.")

    def play_round(self):
        print("\n---\nYour Turn")
        self.player.hand = Hand()

        bet = self.get_bet()

        self.player.draw_card(self.deck)
        self.player.draw_card(self.deck)

        print("\nPlayer's Hand:")
        self.player.show_hand()

        choice = input("\nDo you want to hit or stand? (h/s): ")

        while choice.lower() == "h":
            self.player.draw_card(self.deck)
            print("\nPlayer's Hand:")
            self.player.show_hand()

            if self.player.hand.get_value() > 21:
                print("You busted!")
                break

            choice = input("\nDo you want to hit or stand? (h/s): ")

        print("\n---\nYour Turn ended.")

        if self.player.hand.get_value() <= 21:
            print("\n---\nDealer's Turn")
            self.dealer.hand = Hand()

            self.dealer.draw_card(self.deck)
            self.dealer.draw_card(self.deck, hide_first_card=True)

            print("\nDealer's Hand:")
            self.dealer.show_hand(hide_first_card=True)

            while self.dealer.hand.get_value() < 17:
                self.dealer.draw_card(self.deck)
                print("\nDealer's Hand:")
                self.dealer.show_hand(hide_first_card=True)

                if self.dealer.hand.get_value() > 21:
                    print("Dealer busted!")
                    break

            print("\n---\nDealer's Turn ended.")

        self.evaluate_round(bet)

    def evaluate_round(self, bet):
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        print(f"\n---\nFinal Results:")
        print(f"\n{self.player.name}'s hand:")
        self.player.show_hand()
        print(f"\n{self.dealer.name}'s hand:")
        self.dealer.show_hand()

        if player_value > 21:
            print("\nYou busted! Dealer wins.\n")
            self.player.money -= bet
        elif dealer_value > 21:
            print("\nDealer busted! You win.\n")
            self.player.win_round(bet)
        elif player_value == dealer_value:
            print("\nIt's a tie.\n")
        elif player_value > dealer_value:
            print("\nYou win.\n")
            self.player.win_round(bet)
        else:
            print("\nDealer wins.\n")
            self.player.money -= bet

    def run(self):
        self.setup_game()

        while True:
            self.play_round()
            choice = input("Do you want to play another round? (y/n): ")
            if choice.lower() == "n":
                break

        print("\n---\nTotal Wins:")
        print(f"{self.player.name}: {self.player.wins}")

        net_gain = self.player.money - self.player.initial_money
        print(f"{self.player.name}'s Net Gain: ${net_gain}")

        print(f"{self.dealer.name}: {self.dealer.wins}")

game = BlackjackGame()
game.run()
