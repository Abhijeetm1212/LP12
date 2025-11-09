# 8-Queens Problem using Backtracking
# One Queen is already placed at position (0, 0)

N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row=1):
    # Base case: all queens placed
    if row == N:
        print("Final 8-Queens Solution:\n")
        print_board(board)
        return True

    # Try placing queen in each column for the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

# Initialize board with all 0s
board = [[0] * N for _ in range(N)]

# Pre-place first Queen
board[0][0] = 1

print("Starting with first Queen at (0, 0):\n")
print_board(board)

# Solve for remaining Queens
if not solve(board):
    print("No solution found!")

















































































































































# ---------------------------------------------------------------
# 💡 CONCEPTS IN EASY LANGUAGE (READ BELOW)
# ---------------------------------------------------------------
#
# 🔸 WHAT IS THE 8-QUEENS PROBLEM?
# The 8-Queens problem means placing 8 queens on a chessboard (8x8)
# so that no two queens attack each other.
# A queen attacks another queen if they are in the same:
#   ➤ Row
#   ➤ Column
#   ➤ Diagonal (left or right)
#
# ---------------------------------------------------------------
# 🔸 WHAT IS BACKTRACKING?
# Backtracking is a problem-solving method where:
#   1️⃣ We try to build a solution step by step.
#   2️⃣ If a choice leads to a problem (no solution),
#       we "go back" and try a different path.
# This is similar to exploring a maze and going back if we hit a dead end.
#
# ---------------------------------------------------------------
# 🔸 HOW THIS PROGRAM WORKS:
# - The chessboard is a list of lists called `board`
#   (8x8 grid filled with 0 initially).
# - 0 means an empty cell
# - 1 means a queen is placed there
#
# ---------------------------------------------------------------
# 🔸 MAIN STEPS:
# 1️⃣ Place first queen at (0,0)
# 2️⃣ Move to the next row and try placing a queen in each column.
# 3️⃣ For every position, check if it’s SAFE using `is_safe()` function.
#     - Safe means: no queen in same column, left diagonal, or right diagonal.
# 4️⃣ If it’s safe → place queen and go to the next row.
# 5️⃣ If placing queen in all columns fails → BACKTRACK (remove last queen and try new column).
# 6️⃣ Continue until all 8 queens are placed.
#
# ---------------------------------------------------------------
# 🔸 FUNCTIONS USED:
# ✅ print_board(board):
#    Prints the chessboard with 'Q' for queen and '.' for empty.
#
# ✅ is_safe(board, row, col):
#    Checks if we can place a queen at (row, col)
#    safely without attacks from other queens.
#
# ✅ solve(board, row):
#    Recursive function to place queens row by row using backtracking.
#
# ---------------------------------------------------------------
# 🔸 INPUT:
# No manual input needed in this version.
# The first queen is already placed at (0,0).
#
# (If you want user input, replace top lines with:)
#   N = int(input("Enter board size: "))
#   r0 = int(input("Enter starting queen row: "))
#   c0 = int(input("Enter starting queen column: "))
#   board[r0][c0] = 1
#
# ---------------------------------------------------------------
# 🔸 OUTPUT (Example):
# It will first print the initial board with the first queen:
#
# Starting with first Queen at (0, 0):
# Q . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
#
# Then it will print one final valid arrangement of queens:
#
# Final 8-Queens Solution:
# Q . . . . . . .
# . . . Q . . . .
# . . . . . . Q .
# . Q . . . . . .
# . . . . Q . . .
# . . Q . . . . .
# . . . . . . . Q
# . . . . . Q . .
#
# (The exact arrangement may differ — there are multiple valid solutions.)
#
# ---------------------------------------------------------------
# 🔸 BACKTRACKING EXPLAINED IN SIMPLE WORDS:
# "Try → Check → Go ahead if safe → If wrong, undo → Try next option."
#
# ---------------------------------------------------------------
# 🔸 TIME COMPLEXITY:
# - Roughly O(N!), which means for 8 queens it's fast.
#
# ---------------------------------------------------------------
# 🔸 IMPORTANT CONCEPTS TO REMEMBER:
# ✅ Use recursion for repeated row placements.
# ✅ Use backtracking when the current choice fails.
# ✅ Check safety before placing a queen.
#
# ---------------------------------------------------------------
# END OF EXPLANATION ✅

