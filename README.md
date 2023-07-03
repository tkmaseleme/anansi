# Blackjack Game

This is a command-line implementation of the classic casino game, Blackjack. The game allows players to play rounds of Blackjack against a computer dealer.

## How to Run the Game

To run the game, simply execute the script using Python. Make sure you have Python installed on your system.

```shell
python blackjack.py
```

## Game Rules

The game follows the standard rules of Blackjack:

- The player's goal is to beat the dealer's hand without exceeding a total card value of 21.
- Numbered cards are worth their face value. Face cards (Jack, Queen, and King) are worth 10. Aces can be worth either 1 or 11, whichever is more favorable.
- At the beginning of each round, the player places a bet.
- The player and the dealer are initially dealt two cards each.
- The player can choose to "hit" (draw another card) or "stand" (not draw any more cards).
- If the player's total card value exceeds 21, the player busts and loses the round.
- After the player's turn, the dealer plays according to a fixed set of rules. The dealer must hit until their hand value is 17 or more.
- If the dealer busts, the player wins the round. Otherwise, the values of the player's and dealer's hands are compared, and the higher value wins. If both hands have the same value, it's a tie.

## Classes and Functions

### Card

Represents a single playing card. Each card has a suit and a rank.

### Deck

Represents a deck of 52 cards. The deck can be shuffled, and cards can be drawn from the deck.

### Hand

Represents a hand of cards held by a player. A hand can have multiple cards and can calculate its total value. It can also be displayed.

### Player

Represents a player in the game. Each player has a name and an amount of money. Players can save and load their game data.

### Dealer

Represents the dealer in the game. The dealer is a subclass of the Player class and has an infinite amount of money.

### BlackjackGame

Implements the main logic of the Blackjack game. It handles setting up the game, playing rounds, evaluating the results, and managing player data.

## File Persistence

Player data is saved and loaded using JSON files. Each player's data is stored in a separate file named "<player_name>_data.json". The player's name and money are stored in the file.

## Modifying the Game

If you want to make changes to the game, you can modify the existing code or extend it with additional features. The provided code serves as a starting point for building a more complex Blackjack game.

## Requirements

The game requires Python 3 to run.

## Disclaimer

This implementation of Blackjack is a simplified version and does not cover all possible variations or rules found in real-world casinos.