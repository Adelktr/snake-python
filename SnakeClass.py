from Display import *
from Colors import *

snake_size = 20


class Snake:
    def __init__(self, snake_block, snake_list, direction):
        
        for index, x in enumerate(snake_list):
            body_sprite = pygame.image.load("./assets/snakeBody.png").convert_alpha()
            dis.blit(body_sprite, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))

            if (index == len(snake_list) - 1):
                head_sprite = pygame.image.load("./assets/snakeHead.png").convert_alpha()
                if direction == 'right':
                    rotated_image = pygame.transform.rotate(head_sprite, -90)
                    dis.blit(rotated_image, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))
                elif direction == 'left':
                    rotated_image = pygame.transform.rotate(head_sprite, 90)
                    dis.blit(rotated_image, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))
                elif direction == 'bottom':
                    rotated_image = pygame.transform.rotate(head_sprite, 180)
                    dis.blit(rotated_image, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))
                elif direction == 'up':
                    rotated_image = pygame.transform.rotate(head_sprite, 0)
                    dis.blit(rotated_image, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))
                else:
                    dis.blit(head_sprite, pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]))
                

 