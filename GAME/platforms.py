# Platforms for the game

# Import a library of functions called "pygame"
import pygame
from spritesheet_functions import Spritesheet

GRASS_LEFT = (315, 393, 39, 39)
GRASS_RIGHT = (315, 315, 39, 39)
GRASS_MIDDLE = (276, 315, 39, 39)
MYCELIUM_LEFT = (78, 235, 39, 39)
MYCELIUM_MIDDLE = (39, 235, 39, 39)
MYCELIUM_RIGHT = (78, 155, 39, 39)
BARRIER = (700, 700, 10, 600)
VERTICAL_BARRIER = (475, 0, 26, 78)

# Class for platforms that the bear can stay on
class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        
        # Get the image of the platform
        sprite_sheet = Spritesheet("platforms.png") 

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

# Class for a platform that can move
class MovingPlatform(Platform):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        # Move left or right
        self.rect.x += self.change_x

        # See if player was hit
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.top = self.rect.bottom

        # Move up/down
        self.rect.y += self.change_y

        # Check if player was hit
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Player was hit
            # Reset position
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            # Player was not hit
            else:
                self.player.rect.top = self.rect.bottom
        
        # Stay in the boundaries, reverse direction if necessary        
        if self.rect.bottom > self.boundary_left or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos > self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= 1
        
    
                
    




