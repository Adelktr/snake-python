import pygame
import random
from SnakeClass import *
from MessageClass import *
from Colors import *
from FoodClass import Food

   
clock = pygame.time.Clock()
 
def gameLoop():
    game_over = False
    game_close = False
 
    pos_x = screen_width / 2
    pos_y = screen_height / 2
 
    next_pos_x = 0
    next_pos_y = 0
 
    snake_body_parts = []
    length_of_snake = 1
    random_range_width = round(random.randrange(0, screen_width - 20) / 20.0) * 20.0
    random_range_height = round(random.randrange(0, screen_height - 20) / 20.0) * 20.0

    food = Food(random_range_width, random_range_height)
    score = 0

    direction = ""

    snake_speed = 10
    update_speed = True

    while not game_over:

        # If game over
        while game_close == True:
            dis.fill(green)
            Message("Score : " + str(score), red, "score")
            Message("GAME OVER", red, "title")
            Message("Press R to restart", red, "subtitle")
            Message("Press Q to quit", red, "subtitle2")
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
 
        # Movements + quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    next_pos_x = -snake_size
                    next_pos_y = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    next_pos_x = snake_size
                    next_pos_y = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    next_pos_y = -snake_size
                    next_pos_x = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    next_pos_y = snake_size
                    next_pos_x = 0
                    direction = "bottom"
 
        # if the snake tries to get out of the display
        if pos_x >= screen_width or pos_x < 0 or pos_y >= screen_height or pos_y < 0:
            game_close = True

        # Move the snake
        pos_x += next_pos_x
        pos_y += next_pos_y
        dis.fill(green)
        food.Spawn()
        snake_head = []
        snake_head.append(pos_x)
        snake_head.append(pos_y)
        snake_body_parts.append(snake_head)

        if len(snake_body_parts) > length_of_snake:
            del snake_body_parts[0]
 
        # Check if the head collapse with a part of the snake body
        for snake_part in snake_body_parts[:-1]:
            if snake_part == snake_head:
                game_close = True
 
        # Init snake
        Snake(snake_size, snake_body_parts, direction)
        v = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
 
        # Check if the pos of the snake match with the pos of the food
        if pos_x == food.x and pos_y == food.y:
            random_range_width = round(random.randrange(0, screen_width - 20) / 20.0) * 20.0
            random_range_height = round(random.randrange(0, screen_height - 20) / 20.0) * 20.0

            food = Food(random_range_width, random_range_height)
            food.Spawn()
            length_of_snake += 1
            score += 1

        # Every 5 points, speed increades by 1 
        if score > 0 and score % 5 == 0 and update_speed == True :
           snake_speed += 1
           update_speed = False
        if score % 5 != 0 :
            update_speed = True

        Message("Score : " + str(score), red, "score")
        Message("Speed : " + str(snake_speed), red, "speed")

        pygame.display.update()
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()