from board import Board
from copy import deepcopy


class Life(Board):

    def on_click(self, x, y):
        self.board[y][x] = int(not self.board[y][x])

    def check_neighbours(self, x, y):
        s = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    y + i < 0
                    or y + i >= self.height
                    or x + j < 0
                    or x + j >= self.width
                ):
                    continue
                s += self.board[y + i][x + j]
        s -= self.board[y][x]
        return s

    def regulation(self, board, coords, s):
        x, y = coords
        if s == 3:
            board[y][x] = 1
        elif s < 2 or s > 3:
            board[y][x] = 0

    def next_move(self):
        new_board = deepcopy(self.board)

        for y in range(self.height):
            for x in range(self.width):
                self.regulation(new_board, (x, y), self.check_neighbours(x, y))

        self.board = new_board
