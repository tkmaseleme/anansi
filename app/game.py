from blackjack import BlackjackGame

def main():
    print("Welcome to the Casino!")
    print("Choose a game to play:")
    print("1. Blackjack")
    print("2. Quit")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        blackjack_game = BlackjackGame()
        blackjack_game.play()
    elif choice == '2':
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
