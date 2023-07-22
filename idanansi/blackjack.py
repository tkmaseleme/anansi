#
# The file blackjack.py
#
# Created On Tue Jul 04 2023
#
# Copyright (c) 2023 Trevor K Maseleme
#

import json
import os
from anansi.deck import Deck

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
        self.money = money

    def save_data(self):
        player_data = {
            "name": self.name,
            "money": self.money
        }

        file_path = f"{self.name}_data.json"

        with open(file_path, "w") as file:
            json.dump(player_data, file)

    def load_data(self):
        file_path = f"{self.name}_data.json"

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                player_data = json.load(file)
                self.money = player_data["money"]

class Dealer(Player):
    pass

class BlackjackGame:
    def __init__(self):
        self.player = None
        self.dealer = None
        self.deck = None
        self.minimum_bet = 10

    def setup_game(self):
        self.deck = Deck()
        self.deck.shuffle()

        print("--- Welcome to Blackjack! ---")
        name = input("Enter your name: ")

        file_path = f"{name}_data.json"
        if os.path.exists(file_path):
            self.player = Player(name, 0)
            self.player.load_data()
        else:
            money = int(input("Enter your starting money: $"))
            self.player = Player(name, money)
            self.player.save_data()

        self.dealer = Dealer("Dealer", float("inf"))

    def get_bet(self):
        while True:
            try:
                bet = int(input("\nPlace your bet: $"))
                if bet < self.minimum_bet:
                    print("Invalid bet. The minimum bet is $", self.minimum_bet)
                elif bet > self.player.money:
                    print("Invalid bet. You don't have enough money.")
                else:
                    return bet
            except ValueError:
                print("Invalid bet. Please enter a valid amount.")

    def play_round(self):
        print("\n---\nYour Turn")
        self.player_hand = Hand()

        bet = self.get_bet()

        self.player_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())

        print("\nPlayer's Hand:")
        self.player_hand.show()

        choice = input("\nDo you want to hit or stand? (h/s): ")

        while choice.lower() == "h":
            self.player_hand.add_card(self.deck.draw_card())
            print("\nPlayer's Hand:")
            self.player_hand.show()

            if self.player_hand.get_value() > 21:
                print("You busted!")
                break

            choice = input("\nDo you want to hit or stand? (h/s): ")

        print("\n---\nYour Turn ended.")

        if self.player_hand.get_value() <= 21:
            print("\n---\nDealer's Turn")
            self.dealer_hand = Hand()

            self.dealer_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())

            print("\nDealer's Hand:")
            self.dealer_hand.show(hide_first_card=True)

            while self.dealer_hand.get_value() < 17:
                self.dealer_hand.add_card(self.deck.draw_card())
                print("\nDealer's Hand:")
                self.dealer_hand.show(hide_first_card=True)

                if self.dealer_hand.get_value() > 21:
                    print("Dealer busted!")
                    break

            print("\n---\nDealer's Turn ended.")

        self.evaluate_round(bet)

    def evaluate_round(self, bet):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        print(f"\n---\nFinal Results:")
        print(f"\n{self.player.name}'s hand:")
        self.player_hand.show()
        print(f"\n{self.dealer.name}'s hand:")
        self.dealer_hand.show()

        if player_value > 21:
            print("\nYou busted! Dealer wins.\n")
            self.player.money -= bet
        elif dealer_value > 21:
            print("\nDealer busted! You win.\n")
            self.player.money += bet
        elif player_value == dealer_value:
            print("\nIt's a tie.\n")
        elif player_value > dealer_value:
            print("\nYou win.\n")
            self.player.money += bet
        else:
            print("\nDealer wins.\n")
            self.player.money -= bet

        self.player.save_data()

    def run(self):
        self.setup_game()

        while True:
            if self.player.money <= 0:
                print("You have run out of money. Game over!")
                break

            self.play_round()

            choice = input("Do you want to play another round? (y/n): ")
            if choice.lower() == "n":
                break

        self.player.save_data()

        print(f"\n---\n{self.player.name}'s Money: ${self.player.money}")

        print("\nThanks for playing Blackjack!")
