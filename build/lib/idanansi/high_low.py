from idanansi.deck import Deck

class HighLow:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        print("*******************************************************************")
        print("*                  Welcome to High/Low game!                      *")
        print("*-----------------------------------------------------------------*")
        print("* Guess if the next card is higher or lower than the current card.*")
        print("*                  To exit the game, enter 'exit'.                *")
        print("*-----------------------------------------------------------------*")
        print("*                       Have Fun!!!                               *")
        print("*******************************************************************")

        current_card = self.deck.draw_card()
        while current_card:
            print("\nCurrent card:", current_card)
            guess = input("Will the next card be 'higher' or 'lower'(h/l)? ")
            if guess.lower() == 'exit':
                break

            next_card = self.deck.draw_card()
            if next_card:
                print("Next card:", next_card)
                if self.compare_cards(current_card, next_card) == guess.lower():
                    print("Correct guess!")
                else:
                    print("Wrong guess!")
                current_card = next_card
            else:
                print("No more cards in the deck.")
                break

    @staticmethod
    def compare_cards(card1, card2):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", 
                 "Queen", "King"]
        rank1_index = ranks.index(card1.rank)
        rank2_index = ranks.index(card2.rank)
        if rank1_index < rank2_index:
            return "h"
        elif rank1_index > rank2_index:
            return "l"
        else:
            return "equal"