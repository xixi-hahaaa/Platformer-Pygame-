# Pull individual sprites from a spritesheet

# Import a library of functions called "pygame"
import pygame
import constants

# Create class that grabs objects from a spritesheet
class Spritesheet(object):
    sprite_sheet = None

    def __init__(self, sprite_name):

        # Load the sprite shett
        self.sprite_sheet = pygame.image.load(sprite_name).convert()

    def get_image(self, x, y, width, height):

        # Create a blank image
        image = pygame.Surface([width, height]).convert()

        # Copy sprite from the large sheet to a smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Set transparent colour key
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image
    
