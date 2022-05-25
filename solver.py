from __future__ import print_function
# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None


def check_valid(board, num, pos):
    r, c = pos

    # check row
    for j in range(len(board[0])):
        if c != j and board[r][j] == num:
            return False

    # check col
    for i in range(len(board)):
        if r != i and board[i][c] == num:
            return False

    # check square
    boxr, boxc = r//3, c//3

    for i in range(boxr*3, boxr*3+3):
        for j in range(boxc*3, boxc*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):

    # base case
    find = find_empty(board)
    if not find:
        return True

    row, col = find

    for i in range(1, 10):  # in Sudoku numbers range from 1 through 9 inclusive
        if check_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# print_board(board)
# solve(board)
# print("_____________________________________")
# print_board(board)
