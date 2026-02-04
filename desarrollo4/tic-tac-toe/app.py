"""
tic tac toe game
Author: fabian lopez galvez
"""
#from game_logic import game
from game_logic import play_game
from menu import display_menu

def main():
    """
    Main function to run the Tic Tac Toe game
    """
    while True:
        choice = display_menu()
        if choice == 1:
            play_game(1)
        elif choice == 2:
            play_game(2)
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()