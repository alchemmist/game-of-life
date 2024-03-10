import pygame
from life import Life
from config import *


def main():
    board = Life(
        CELLULAR_FIELD_WIDTH, CELLULAR_FIELD_HEIGHT, 
        left=LEFT_INDENT, top=TOP_INDENT, 
        cell_size=CELL_SIZE, 
        border=BORDER_WIDTH,
    )

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    speed = START_SPEED

    evolve = False
    running = True

    while running:
        evole = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==  pygame.MOUSEBUTTONUP and event.button == 3:
                evolve = True
            if event.type ==  pygame.MOUSEWHEEL:
                speed -= event.y
                if speed <= 0:
                    speed = 1
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    evolve = not evolve

        if pygame.mouse.get_pressed()[0]:
            board.get_click(pygame.mouse.get_pos())

        if evolve:
            board.next_move()
            clock.tick(speed)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
