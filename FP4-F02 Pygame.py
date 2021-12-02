import pygame
import random

RED = (255, 0, 0)
WHITE = (255, 255, 255)



class sqaure:
    
    
    def __init__(self):
        global surface
        surface = pygame.display.set_mode(size=(800, 600))
        pygame.draw.rect(surface, RED, pygame.Rect(0, 0, 800, 600), 5)
        pygame.display.flip()
        pygame.draw.circle(surface, WHITE, (400, 300), 20)
        pygame.display.flip()
    def move(self):
      self.move_x = random.randrange(5, 10)
      self.move_y = random.randrange(5, 10)
      self.x += self.move_x
      self.y += self.move_x
      if self.x < 0:
          self.x = 0
        elif 
    

sqaure()