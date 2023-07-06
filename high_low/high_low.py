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

class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        print("Welcome to the War Card Game!")
        print("----------------------------")
        player_name = input("Enter your name: ")
        print(f"Hello {player_name}! You'll be playing against Aaron.")

        player_hand = []
        computer_hand = []

        # Deal cards to players
        while len(self.deck.cards) > 0:
            player_hand.append(self.deck.draw_card())
            computer_hand.append(self.deck.draw_card())

        player_score = 0
        computer_score = 0

        # Compare cards
        for i in range(len(player_hand)):
            player_card = player_hand[i]
            computer_card = computer_hand[i]

            print(f"\nYour card: {player_card}")

            # Get the player's guess
            player_guess = input("Do you think Aaron's card is higher or lower? (h/l): ")

            print(f"Aaron's card: {computer_card}")

            # Compare ranks
            if player_card.rank > computer_card.rank:
                if player_guess == 'h':
                    print("Your guess is correct! You win the round!")
                    player_score += 1
                else:
                    print("Your guess is incorrect! Aaron wins the round!")
                    computer_score += 1
            elif player_card.rank < computer_card.rank:
                if player_guess == 'l':
                    print("Your guess is correct! You win the round!")
                    player_score += 1
                else:
                    print("Your guess is incorrect! Aaron wins the round!")
                    computer_score += 1
            else:
                print("It's a tie!")

        print("\n-------------------------")
        print("Game Over!")
        print(f"Your score: {player_score}")
        print(f"Aaron's score: {computer_score}")

        # Determine the winner
        if player_score > computer_score:
            print(f"Congratulations {player_name}! You win the game!")
        elif player_score < computer_score:
            print("Aaron wins the game. Better luck next time!")
        else:
            print("It's a tie!")

# Start the game
game = WarGame()
game.play()
