"Author: fabian lopez galvez "
"here goes the game logic for ticatctoe"
import board

def game():
    """
    Heres lives the main game loop
    """
    turns = 0
    dboard = {x:str(x) for x in range(9)}
    x_player = "X"
    o_player ="O"
    current_player = x_player
    while turns<9:
        board.display_board(dboard)
        valid_move = False
        while not valid_move:
            valid_move = board.player_turn (current_player, dboard)
        turns += 1
        if current_player == x_player:
            current_player = o_player
        else:
            current_player = x_player

if __name__=="__main__":
    game()



