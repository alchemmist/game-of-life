import pygame


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30, border=1):
        self.width = width
        self.height = height
        self.border = border
        self.board = [[0] * width for _ in range(height)]

        self.left = left
        self.top = top
        self.cell_size = cell_size

        self.last_coords = None

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen: pygame.surface.Surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.border != 0:
                    pygame.draw.rect(
                        screen,
                        pygame.Color("white"),
                        (
                            self.left + x * self.cell_size,
                            self.top + y * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                        self.border,
                    )
                m = 0 if self.border <= 0 else 1
                pygame.draw.rect(
                    screen,
                    pygame.Color("green" if self.board[y][x] else "black"),
                    (
                        self.left + x * self.cell_size + self.border,
                        self.top + y * self.cell_size + self.border,
                        self.cell_size - m - self.border,
                        self.cell_size - m - self.border,
                    ),
                )

    def get_cell(self, mouse_pos):
        x, y = mouse_pos

        if (
            x > ((self.cell_size * self.width) + self.left)
            or x < self.left
            or y > ((self.cell_size * self.height) + self.top)
            or y < self.top
        ):
            return

        x -= self.left
        y -= self.top

        return x // self.cell_size, y // self.cell_size

    def get_click(self, mouse_pos):
        coords = self.get_cell(mouse_pos)
        if coords is None or coords == self.last_coords:
            return
        self.last_coords = coords

        try:
            self.on_click(*coords)
        except IndexError:
            pass
     
    def on_click(self, x, y):
        pass


