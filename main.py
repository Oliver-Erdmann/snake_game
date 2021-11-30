import pygame
import random

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (137, 207, 240)
green = (0, 255, 0)
red = (255, 0, 0)
brown = (134, 102, 75)

board_width = 500
board_height = 500

pygame.init()

board = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("woah woah woah snake snake snake")

apples = 10
snake_head = 10
snake_speed = 9

font_style = pygame.font.SysFont("arial", 20)

def message(msg, color, offset):
    mesg = font_style.render(msg, True, color)
    board.blit(mesg, [board_width/3, board_height/3+offset])

def my_score(score):
    message = font_style.render("your score is " + str(score), True, black)
    board.blit(message, [10, 10])

def my_snake(apples, snake_list):
    for x in snake_list:
        pygame.draw.rect(board, brown, [x[0], x[1], apples, apples])

def main_game():
    run = True
    stop = False

    x1 = board_width/2
    y1 = board_height/2

    y1_change = 0
    x1_change = 0

    snake = []
    snake_length = 1

    ran_x = round(random.randrange(0, board_width-snake_head)/10.0)*10.0
    ran_y = round(random.randrange(0, board_height-snake_head)/10.0)*10.0

    while run == True:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                pygame.display.flip()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_head

                elif event.key == pygame.K_a:
                    x1_change = -snake_head
                    y1_change = 0

                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = +snake_head

                elif event.key == pygame.K_d:
                    x1_change = +snake_head
                    y1_change = 0

        board.fill(blue)

        if x1 < 0 or x1 > board_width or y1 < 0 or y1 > board_height:
            board.fill(black)
            message("go cry to your mother you baby", white, 0)
            message("don't ever come back here", white, 20)

        if x1 == ran_x and y1 == ran_y:
            ran_x = round(random.randrange(0, board_width - snake_head) / 10.0) * 10.0
            ran_y = round(random.randrange(0, board_height - snake_head) / 10.0) * 10.0
            snake_length = snake_length + 1

        x1 += x1_change
        y1 += y1_change
        pygame.draw.rect(board, black, pygame.Rect(ran_x, ran_y, apples, apples))
        snake_face = []
        snake_face.append(int(x1))
        snake_face.append(int(y1))
        snake.append(snake_face)

        if len(snake) > snake_length:
            del snake[0]

        for x in snake[: - 1]:
            for x in snake[: - 1]:
                if x == snake_face:
                    board.fill(black)
                    message("go cry to your mother you baby", white, 0)
                    message("don't ever come back here", white, 20)
                    pygame.display.update()
                    run = False

        my_snake(apples, snake)
        my_score(snake_length - 1)
        pygame.display.update()
        clock.tick(snake_speed)


main_game()