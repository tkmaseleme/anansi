from deck import Deck
from player import Player

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = None
        self.cpu = Player("CPU", 0)

    def play(self):
        print("Welcome to Blackjack!")

        # Get player name
        player_name = input("Enter your name: ")

        # Get player initial money
        while True:
            try:
                player_money = float(input("Enter the amount of money you have: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        self.player = Player(player_name, player_money)

        # Game loop
        while True:
            self.deck.create_deck()
            self.deck.shuffle()

            self.player.clear_cards()
            self.cpu.clear_cards()

            # Place bets
            while True:
                try:
                    bet = float(input("Place your bet: "))
                    if bet <= self.player.money:
                        self.player.money -= bet
                        break
                    else:
                        print("Insufficient funds. Please place a valid bet.")
                except ValueError:
                    print("Invalid input. Please enter a valid bet.")

            # Deal initial cards
            self.player.add_card(self.deck.draw_card())
            self.cpu.add_card(self.deck.draw_card())
            self.player.add_card(self.deck.draw_card())
            self.cpu.add_card(self.deck.draw_card())

            print("\n--- Initial Hands ---")
            print(f"Player: {', '.join(str(card) for card in self.player.cards)}")
            print(f"CPU: {self.cpu.cards[0]} and one hidden card\n")

            # Player's turn
            while True:
                print(f"Player's hand value: {self.player.get_hand_value()}")
                choice = input("Do you want to hit or stand? (h/s): ").lower()
                if choice == "h":
                    self.player.add_card(self.deck.draw_card())
                    print(f"\nPlayer drew: {self.player.cards[-1]}\n")
                    if self.player.get_hand_value() > 21:
                        print("Player busts! CPU wins.")
                        break
                elif choice == "s":
                    break
                else:
                    print("Invalid choice. Please enter 'h' to hit or 's' to stand.")

            # CPU's turn
            if self.player.get_hand_value() <= 21:
                print("\n--- CPU's Turn ---")
                print(f"CPU's hand: {', '.join(str(card) for card in self.cpu.cards)}\n")
                while self.cpu.get_hand_value() < 17:
                    self.cpu.add_card(self.deck.draw_card())
                    print(f"CPU drew: {self.cpu.cards[-1]}")
                print(f"\nCPU's hand value: {self.cpu.get_hand_value()}\n")

                if self.cpu.get_hand_value() > 21:
                    print("CPU busts! Player wins.")
                    self.player.money += 2 * bet
                elif self.cpu.get_hand_value() > self.player.get_hand_value():
                    print("CPU wins.")
                elif self.cpu.get_hand_value() < self.player.get_hand_value():
                    print("Player wins!")
                    self.player.money += 2 * bet
                else:
                    print("It's a tie!")

            print(f"\nPlayer's money: {self.player.money}")

            # Check if player wants to play again
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice != "y":
                print("Thank you for playing!")
                break

            print("\n")

# Main program
if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
