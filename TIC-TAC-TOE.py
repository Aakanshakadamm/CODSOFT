import random

def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

   
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif check_tie(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '

        if score > best_score:
            best_score = score
            best_move = (i, j)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    while True:
        print_board(board)

        if player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player = 'O'
        else:
            row, col = best_move(board)
            board[row][col] = 'O'
            player = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
