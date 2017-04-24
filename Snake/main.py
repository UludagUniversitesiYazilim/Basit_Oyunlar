import pygame
import Snake
import time


def main():
    pygame.init()
    game_board = pygame.display.set_mode([1024, 768], pygame.HWSURFACE)
    exit_game = False
    clock = pygame.time.Clock()
    foo = 0
    kdowned = "d"
    snake = Snake.Snake()
    time1 = time.time()

    while not exit_game:
        time2 = time.time()
        if time2 - time1 > 1:
            print(foo)
            break
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_game = True

            if e.type == pygame.KEYDOWN:
                kdowned = e.unicode

        if kdowned == "w":
            snake.set_direction(0,-1)
        elif kdowned == "s":
            snake.set_direction(0, 1)
        if kdowned == "a":
            snake.set_direction(-1, 0)
        elif kdowned == "d":
            snake.set_direction(1, 0)


        game_board.fill((255, 255, 255))
        for i in snake.get_coordinates:
            pygame.draw.rect(game_board, (0, 123, 0), (i[0]*20, i[1]*20, 20, 20))

        snake.move_snake()
        pygame.display.update()


        if snake.get_speed < 40:
            clock.tick(snake.get_speed)
        else:
            break

        foo += 1
        if foo%5 == 0:
            snake.eat()


    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
