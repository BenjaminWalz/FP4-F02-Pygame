import pygame
import random

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()




class sqaure:
    
    
    def __init__(self, WIDTH, HEIGHT):

        
        global surface
        surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        pygame.draw.rect(surface, RED, pygame.Rect(0, 0, 800, 600), 5)
        pygame.display.flip()
        pygame.display.flip()
    
    
    
    def move(self):
       pygame.draw.circle(surface, WHITE, (400, 300), 20)
       pygame.display.flip()
       self.move_x = random.randrange(1, 4)
       self.move_y = random.randrange(1, 4)
       self.x = self.move_x
       self.y = self.move_y
       
       if self.x < 0: self.x = 0
       elif self.x > 800: self.x = 600
        
       if self.y < 0: self.y = 0
       elif self.y > 600: self.y = 600
       
       
       
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               go = False
        
        

def main():
    sqaure(800, 600).move()

    go = True
    while go == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    pygame.display.update()
    clock.tick(60)
           
           
          
    

#sqaure(800, 600).move()
main()