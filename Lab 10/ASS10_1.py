N = 8 

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    #column 
    for i in range(row):
        if board[i][col]:
            return False

    # upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    #upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row=0):
    if row == N:
        print_solution(board)
        return True  # To find all solutions, change to False and remove return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = True
            solve_n_queens(board, row + 1)
            board[row][col] = False  # Backtracking

    return False

# no queens
board = [[False] * N for _ in range(N)]
solve_n_queens(board)
