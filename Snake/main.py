import pygame
import time
from Snake import CSnake
from Snake import Const


def main():
    zit = {119: 115, 273: 274,
           115: 119, 274: 273,
           97: 100, 276: 275,
           100: 97, 275: 276}

    pygame.init()
    game_board = pygame.display.set_mode([550, 550], pygame.HWSURFACE | pygame.SWSURFACE)
    exit_game = False
    clock = pygame.time.Clock()
    foo = 0
    bar = 0
    key_downed = 100
    snake = CSnake.Snake()
    time1 = time.time()

    while not exit_game:
        time2 = time.time()

        if time2 - time1 > 1:
            pygame.display.set_caption(str(bar) + " Saniye - " + " Score: " + str(snake.get_score))
            foo = 0
            bar += 1
            time1 = time2

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_game = True

            if e.type == pygame.KEYDOWN:
                if not zit[key_downed] == e.key:
                    key_downed = e.key
                    break

        if snake.get_speed < 80:
            if key_downed == 119 or key_downed == 273:
                snake.set_direction(0, -1)
            elif key_downed == 115 or key_downed == 274:
                snake.set_direction(0, 1)
            if key_downed == 97 or key_downed == 276:
                snake.set_direction(-1, 0)
            elif key_downed == 100 or key_downed == 275:
                snake.set_direction(1, 0)

            game_board.fill(Const.PURPLE)
            for i in snake.get_coordinates:
                pygame.draw.rect(game_board, Const.GREY, (i[0] * 10, i[1] * 10, 10, 10))

            pygame.draw.rect(game_board, Const.ORANGE, (snake.get_coordinates[0][0] * 10,
                                                          snake.get_coordinates[0][1] * 10, 10, 10))

            pygame.draw.ellipse(game_board, Const.RED,
                                (snake.get_apple.coords[0] * 10, snake.get_apple.coords[1] * 10, 10, 10))

            if snake.move_snake() == -1:
                exit_game = True
            pygame.display.update()
            clock.tick(15)
        else:
            exit_game = True

        foo += 1

    pygame.time.wait(2000)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
