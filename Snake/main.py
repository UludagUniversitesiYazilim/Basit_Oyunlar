import pygame
import Snake
import time


def main():
    pygame.init()
    game_board = pygame.display.set_mode([550, 550], pygame.HWSURFACE | pygame.SWSURFACE | pygame.NOFRAME)
    exit_game = False
    clock = pygame.time.Clock()
    foo = 0
    kdowned = "d"
    snake = Snake.CSnake()
    time1 = time.time()

    while not exit_game:
        time2 = 0
        if time2 - time1 > 1:
            print(foo)
            exit_game = True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_game = True

            if e.type == pygame.KEYDOWN:
                kdowned = e.unicode

        if snake.get_speed < 40:
            if kdowned == "w":
                snake.set_direction(0, -1)
            elif kdowned == "s":
                snake.set_direction(0, 1)
            if kdowned == "a":
                snake.set_direction(-1, 0)
            elif kdowned == "d":
                snake.set_direction(1, 0)

            game_board.fill((255, 255, 255))
            for i in snake.get_coordinates:
                pygame.draw.rect(game_board, (0, 123, 0), (i[0] * 10, i[1] * 10, 10, 10))

            pygame.draw.ellipse(game_board, (255, 0, 0),
                                (snake.get_apple.coords[0] * 10, snake.get_apple.coords[1] * 10, 10, 10))

            if snake.move_snake() == -1:
                exit_game = True
            pygame.display.update()
            clock.tick(snake.get_speed)
        else:
            exit_game = True

        foo += 1

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
