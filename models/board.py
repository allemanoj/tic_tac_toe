# models/board.py

from utils.exceptions import InvalidMoveError

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.moves_made = 0

    def display(self):
        print("\n")
        for i in range(self.size):
            print(" | ".join(self.grid[i]))
            if i < self.size - 1:
                print("-" * (self.size * 4 - 3))
        print("\n")

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == ' '

    def make_move(self, row, col, symbol):
        if not self.is_valid_move(row, col):
            raise InvalidMoveError(f"Cell ({row+1},{col+1}) is already filled or out of bounds.")
        self.grid[row][col] = symbol
        self.moves_made += 1

    def check_winner(self, symbol):
        # Check rows and columns
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True

        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True

        return False

    def is_draw(self):
        return self.moves_made == self.size * self.size

    def reset(self):
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.moves_made = 0
