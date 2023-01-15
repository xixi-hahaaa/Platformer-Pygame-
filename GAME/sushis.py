# Sushi for the game

# Import a library of functions calledn "pygame"
import pygame
from spritesheet_functions import Spritesheet

SUSHI = (0, 0, 32, 32)

# Class for platforms that the bear can stay on
class Sushi(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        
        # Get the image of the platform
        sprite_sheet = Spritesheet("sushi.png") 

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()


    
                
    


