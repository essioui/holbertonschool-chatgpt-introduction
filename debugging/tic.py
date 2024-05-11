#!/usr/bin/python3

def print_board(board):
    # Function description: Prints the Tic-Tac-Toe board.
    # Parameters:
    #   board (list): The 3x3 list representing the game board.
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Function description: Checks if there is a winner in the Tic-Tac-Toe game.
    # Parameters:
    #   board (list): The 3x3 list representing the game board.
    # Returns:
    #   bool: True if there is a winner, False otherwise.
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    # Function description: Runs the Tic-Tac-Toe game.
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

# Run the Tic-Tac-Toe game
tic_tac_toe()
