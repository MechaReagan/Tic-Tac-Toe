# for i in range(len(board)):
#     if(board[i] == "-" ):
#         print("-", " is Found at Position " , i + 1)


def check_for_victory(player, x_positions, o_positions):
    winning_positions = [[1, 2, 3], [1, 4, 7], [3, 6, 9], [7, 8, 9], [4, 5, 6], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
    for winning in winning_positions:
        if all(value in x_positions for value in winning) or all(value in o_positions for value in winning):
            print(f"{player} wins!")
            print(board)
            return True
    if board.count("X") + board.count("O") == 9:
        print("It's a draw!")
        print(board)
        return True
    return False


def place_piece(choice, player):
    global board
    positions = "1 2 3 4 5 6 7 8 9"
    if choice in board and (choice in positions):
        board = board.replace(choice, player)
    else:
        print("That position already has a piece on it or I don't recognize it. You lose your turn!\n")


def player_vs_player(x_positions, o_positions):
    while True:
        print(board)
        choice = input("Player X:\nPlease pick which position you would like to place your piece: ")
        if choice in board:
            try:
                x_positions.append(int(choice))
            except ValueError:
                pass
        place_piece(choice, player="X")
        if check_for_victory("X", x_positions, o_positions) is True:
            break
        print(board)
        choice = input("Player O:\nPlease pick which position you would like to place your piece: ")
        if choice in board:
            try:
                o_positions.append(int(choice))
            except ValueError:
                pass
        place_piece(choice, player="O")
        if check_for_victory("O", x_positions, o_positions) is True:
            break


print(' _   _      _             _             \n'
'| | (_)    | |           | |            \n'
'| |_ _  ___| |_ __ _  ___| |_ ___   ___ \n'
'| __| |/ __| __/ _` |/ __| __/ _ \ / _ l\n'
'| |_| | (__| || (_| | (__| || (_) |  __/\n'
' \__|_|\___|\__\__,_|\___|\__\___/ \___|\n')

print(f"Welcome to Tic-Tac-Toe, the ultimate game of skill. Below, you'll see the board, \n"
      f"     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____"
      f"\n     |     |     \n  7  |  8  |  9  \n     |     |     \n"
      f"Simply type in the corresponding number  in order to place your piece in that spot.\n"
      f"Have a wonderful game, and thank you for playing!\n\n")

while True:
    board = "     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  " \
            "\n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     \n"
    x = []
    o = []
    begin = input("Please hit enter to begin.")
    player_vs_player(x, o)
    go_again = input("\nWould you like to play again? (Y or N): ")
    if go_again.lower() == "y":
        pass
    else:
        break