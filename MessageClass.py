from Display import *

class Message:
    def __init__(self, msg, color, pos):
        font = pygame.font.Font(None, 25)
        text = font.render(msg, True, color)

        if pos == "score" :
            text_rect = text.get_rect(topleft=(10, 10))

        if pos == "speed" :
            text_rect = text.get_rect(topleft=(100, 10))

        if pos == "title" :
            text_rect = text.get_rect(center=(screen_width/2, screen_height/3))

        if pos == "subtitle" :
            text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

        if pos == "subtitle2" :
            text_rect = text.get_rect(center=(screen_width/2, screen_height/2 + 20))
        
        dis.blit(text, text_rect)
 