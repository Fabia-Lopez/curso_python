def display_board(dboard:dict)->None:
    d= dboard

    print(f"{d[0]:2s}|{d[1]:2s}|{d[2]:2s}")
    print("--+---+---")

    print(f"{d[3]:2s}|{d[4]:2s}|{d[5]:2s}")
    print("--+---+---")

    print(f"{d[6]:2s}|{d[7]:2s}|{d[8]:2s}")

def player_turn(player:str, dboard:dict)->int:
    

if _name_=="_main_":
    board ={x:str(x)for x in range(9)}
    display_board(board)
    board[0]='X'
    board[4]='O'
    display_board(board)
