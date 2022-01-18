import pygame
import pygame.display
import pygame.transform
import pygame.sprite

from pygame.locals import *

class Level():
    def __init__(self):
        super().__init__()
        self.curr_level = 1
        self.part = 1

        self.ground = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_{self.curr_level}/part_{self.part}/ground.png"), 0, 2
            )
        self.sky = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_{self.curr_level}/part_{self.part}/sky.png"), 0, 2
            )
        self.curr_level = 1
        self.part = 1


    def new_part(self):
        self.part += 1
        self.ground = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_1/part_{self.part}/ground.png"), 0, 2
            )
        self.sky = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_1/part_{self.part}/sky.png"), 0, 2
            )
        return(self.ground, self.sky)
    def old_part(self):
        
        self.part -= 1
        self.ground = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_1/part_{self.part}/ground.png"), 0, 2
            )
        self.sky = pygame.transform.rotozoom(
            pygame.image.load(f"assets/levels/level_1/part_{self.part}/sky.png"), 0, 2
            )
        return(self.ground, self.sky)

    
        
        
