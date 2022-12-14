from Display import *
from SnakeClass import *

class Food:
    def __init__(self, foodx, foody):
        self.x = foodx
        self.y = foody
    def Spawn(self):
        fruit_sprite = pygame.image.load("./assets/apple.png").convert_alpha()
        dis.blit(fruit_sprite, pygame.draw.rect(dis, green, [self.x, self.y, snake_size, snake_size]))

