import pygame
import time
import random

pygame.init()

back_color = (0, 153, 51)
snake_color = (255, 153, 102)
snack_color = (255, 0, 255)
lose_color = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 102)

display_width = 600
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hungry python in python using pygame')

clock = pygame.time.Clock()

snake_block_size = 15


font_style = pygame.font.SysFont('bahnschrift', 30)
score_font = pygame.font.SysFont('comicsansms', 35)

def your_score(score):
    value = score_font.render(f'Your score: {score}', True, yellow)
    display.blit(value, [0, 0])

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_block_size, snake_block_size])

def lose_message():
    mesg_1 = font_style.render('You lost!', True, lose_color)
    mesg_2 = font_style.render('Press "q" to quit the game.', True, white)
    mesg_3 = font_style.render('Press "p" to play again.', True, white)
    display.blit(mesg_1, [display_width / 2 - 300, display_height / 3])
    display.blit(mesg_2, [display_width / 2 - 300, display_height / 3 + 50])
    display.blit(mesg_3, [display_width / 2 - 300, display_height / 3 + 100])
    pygame.display.update()

def intro_message():
    i_mesg_1 = font_style.render('Your snake is orange and snacks are pink.', True, yellow)
    i_mesg_2 = font_style.render('Eat as much as you can!', True, yellow)
    i_mesg_3 = font_style.render('Use arrows to move the snake.', True, yellow)
    i_mesg_4 = font_style.render('Game will start shortly.', True, yellow)
    display.blit(i_mesg_1, [display_width / 2 - 300, display_height / 3])
    display.blit(i_mesg_2, [display_width / 2 - 300, display_height / 3 + 50])
    display.blit(i_mesg_3, [display_width / 2 - 300, display_height / 3 + 100])
    display.blit(i_mesg_4, [display_width / 2 - 300, display_height / 3 + 150])
    pygame.display.update()

def game_loop():
    game_over = False
    game_close = False,

    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    snake_length = 1
    snake_speed = 12

    foodx = round(random.randrange(0, display_width - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
    foody = round(random.randrange(0, display_height - snake_block_size) / float(snake_block_size)) * float(snake_block_size)

    while not game_over:
        while game_close == True:
            display.fill(back_color)
            lose_message()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block_size
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(back_color)
        pygame.draw.rect(display, snack_color, [foodx, foody, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > snake_length:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
        snake(snake_block_size, snake_List)
        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
            foody = round(random.randrange(0, display_height - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
            snake_length += 1
            snake_speed += 0.5
        clock.tick(snake_speed)
    pygame.quit()
    quit()
display.fill(back_color)
intro_message()
time.sleep(5)
game_loop()
