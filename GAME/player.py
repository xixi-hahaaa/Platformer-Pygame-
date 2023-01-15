# Player for Bear Run - Panda Bear

# Import a library of functions
import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import Spritesheet

class Player(pygame.sprite.Sprite):

    # Score
    score = 0

    # Player speed
    change_x = 0
    change_y = 0

    # Holds sprites for animated walk left/right
    walking_frames_1 = []
    walking_frames_r = []

    # Player starting direction
    direction = "R"

    # Sprites to collide with
    level = None

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = Spritesheet("bear.png")
        # Load sprites to a list: walking left
        image = sprite_sheet.get_image(432, 240, 48, 48)
        self.walking_frames_1.append(image)
        image = sprite_sheet.get_image(480, 240, 48, 48)
        self.walking_frames_1.append(image)
        image = sprite_sheet.get_image(528, 240, 48, 48)
        self.walking_frames_1.append(image)

        # Load sprites to a list: walking right
        image = sprite_sheet.get_image(432, 288, 48, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(480, 288, 48, 48)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(528, 288, 48, 48)
        self.walking_frames_r.append(image)

        # Set the image the player will begin with
        self.image = self.walking_frames_r[0]

        # Referance to the image rect
        self.rect = self.image.get_rect()
        

    def update(self):
        # Movement
        self.gravity()

        # Move left or right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30 ) % len(self.walking_frames_1)
            self.image = self.walking_frames_1[frame]

        # Check for collision
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Moving right, set right side to left side of the collided item
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Moving left, set left side to right side
                self.rect.left = block.rect.right

        # Check for collision with sushi
        sushi_hit_list = pygame.sprite.spritecollide(self, self.level.sushi_list, True)
        for food in sushi_hit_list:
            # Remove the sushi and add to score
            self.level.sushi_list.remove(food)
            self.score = self.score + 1
            pygame.display.update()

        # Move up or down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for  block in block_hit_list:
            # Moving up/down, reset to top/bottom of object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def gravity(self):
        # Gravity effect 
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        # Check if player is on the ground
        if self.rect.y >= constants.HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.HEIGHT - self.rect.height

    def jump(self):
        # When the user wants the bear to jump
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.HEIGHT:
            self.change_y = -10

    def move_left(self):
        # Move left
        self.change_x = -5
        self.direction = "L"

    def move_right(self):
        # Move right
        self.change_x = 5
        self.direction = "R"

    def stop(self):
        # Stop moving when user lets up on arrow keys
        self.change_x = 0
            

        
        
            

            
            
