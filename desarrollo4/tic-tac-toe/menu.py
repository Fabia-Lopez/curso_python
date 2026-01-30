
"""
Menu in main window
"""

def display_menu()->int:
    """
    display_menu function shows the main menu and gets user choice
    """
    print("Welcome to Tic Tac Toe!")
    print("1. One player game")
    print("2. two player game")
    print("3. Exit")
    choice = input("Select an option (1-3): ")
    return int(choice)


if __name__ == "__main__":
    display_menu()