import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)



class sqaure:
    
    
    def __init__(self):
        global surface
        surface = pygame.display.set_mode(size=(800, 600))
        pygame.draw.rect(surface, RED, pygame.Rect(0, 0, 800, 600), 5)
        pygame.display.flip()
        
    def move(self, x, y):
        move = pygame.draw.rect(surface, WHITE, pygame.Rect(x, y, 50, 50))
        pygame.display.flip()
        key = pygame.key.get_pressed()
        go = True
        
        while go == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    go = False
                elif event.type == pygame.KEYDOWN:
                    y = y - 1
                    return y
sqaure().move(100, 100)
    
    
    
    
    
    
    