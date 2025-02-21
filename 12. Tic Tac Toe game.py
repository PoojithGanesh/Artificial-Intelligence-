def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")
            continue

        if board[row][col] != " ":
            print("Cell is already taken! Try again.")
            continue

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = 1 - turn

if __name__ == "__main__":
    tic_tac_toe()
