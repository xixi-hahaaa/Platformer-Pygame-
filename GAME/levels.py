# Classes for the game levels

# Import a library of functions
import pygame
import random
import platforms
import constants
import sushis

class Level():
    # List of sprites used in all levels
    platform_list = None
    sushi_list = None

    # Background image
    background = None

    # Shift world
    world_shift = 0
    level_limit = 100

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.sushi_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.sushi_list.update()

    def draw(self, screen):
        # Background and shift to perspective
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift // 3, 0))
        
        # Draw sprites
        self.platform_list.draw(screen)
        self.sushi_list.draw(screen)

    def shift_world(self, shift_x):
        # Shift amount
        self.world_shift += shift_x

        # Shift all sprite lists
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for sushi in self.sushi_list:
            sushi.rect.x += shift_x

# Level One
class Level_01(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("hills.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000  # End of level

        # Array with all the platforms with the (x, y) coordinates
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 538, 500],
                  [platforms.GRASS_RIGHT, 576, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 838, 400],
                  [platforms.GRASS_RIGHT, 876, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1038, 500],
                  [platforms.GRASS_RIGHT, 1076, 500],
                  [platforms.BARRIER, 110, 0],
                  [platforms.GRASS_LEFT, 1100, 300],
                  [platforms.GRASS_MIDDLE, 1138, 300],
                  [platforms.GRASS_RIGHT, 1176, 300],
                  [platforms.GRASS_LEFT, 1200, 200],
                  [platforms.GRASS_MIDDLE, 1238, 200],
                  [platforms.GRASS_MIDDLE, 1276, 200],
                  [platforms.GRASS_MIDDLE, 1300, 200],
                  [platforms.GRASS_MIDDLE, 1338, 200],
                  [platforms.GRASS_MIDDLE, 1250, 450],
                  [platforms.VERTICAL_BARRIER, 1200, 522]
                  ]

        # Add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with all the sushi and coordinates for the sushi
        point = [ [sushis.SUSHI, 510, 470],
                  [sushis.SUSHI, 570, 470],
                  [sushis.SUSHI, 830, 330],
                  [sushis.SUSHI, 870, 370],
                  [sushis.SUSHI, 1000, 470],
                  [sushis.SUSHI, 1050, 470],
                  [sushis.SUSHI, 1950, 570],
                  [sushis.SUSHI, 1950, 470],
                  [sushis.SUSHI, 1950, 370],
                  [sushis.SUSHI, 1250, 420],
                  [sushis.SUSHI, 1138, 270],
                  [sushis.SUSHI, 1210, 170],
                  [sushis.SUSHI, 1250, 170],
                  [sushis.SUSHI, 1290, 170],
                  [sushis.SUSHI, 1370, 570],
                  [sushis.SUSHI, 1470, 570],
                  ]

        # Add sushi
        for sushi in point:
            food = sushis.Sushi(sushi[0])
            food.rect.x = sushi[1]
            food.rect.y = sushi[2]
            food.player = self.player
            self.sushi_list.add(food)

# Level Two
class Level_02(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("autumn.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1200  # End of level

        # Array with all the platforms with the (x, y) coordinates
        level = [ [platforms.MYCELIUM_LEFT, 500, 500],
                  [platforms.BARRIER, 110, 0],
                  [platforms.MYCELIUM_MIDDLE, 539, 500],
                  [platforms.MYCELIUM_MIDDLE, 576, 500],
                  [platforms.MYCELIUM_LEFT, 800, 400],
                  [platforms.MYCELIUM_MIDDLE, 839, 400],
                  [platforms.MYCELIUM_RIGHT, 876, 400],
                  [platforms.MYCELIUM_LEFT, 1000, 500],
                  [platforms.MYCELIUM_MIDDLE, 1039, 500],
                  [platforms.MYCELIUM_RIGHT, 1076, 500],
                  [platforms.VERTICAL_BARRIER, 1090, 522],
                  [platforms.VERTICAL_BARRIER, 1120, 422],
                  [platforms.MYCELIUM_LEFT, 1100, 400],
                  [platforms.MYCELIUM_LEFT, 1150, 300],
                  [platforms.MYCELIUM_LEFT, 1200, 200],
                  [platforms.MYCELIUM_LEFT, 1350, 100],
                  [platforms.MYCELIUM_MIDDLE, 1490, 100],
                  [platforms.MYCELIUM_RIGHT, 1238, 200],
                  [platforms.MYCELIUM_RIGHT, 1138, 400],
                  [platforms.MYCELIUM_MIDDLE, 1650, 100],
                  [platforms.MYCELIUM_MIDDLE, 1700, 100],
                  [platforms.MYCELIUM_MIDDLE, 1820, 100],
                  [platforms.MYCELIUM_MIDDLE, 1890, 100],
                  [platforms.MYCELIUM_MIDDLE, 2040, 100]                  
                  ]

        # Add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with all the sushi and coordinates for the sushi
        point = [ [sushis.SUSHI, 510, 470],
                  [sushis.SUSHI, 570, 470],
                  [sushis.SUSHI, 1150, 270],
                  [sushis.SUSHI, 1100, 370],
                  [sushis.SUSHI, 1000, 470],
                  [sushis.SUSHI, 1400, 70],
                  [sushis.SUSHI, 1500, 70],
                  [sushis.SUSHI, 1550, 70],
                  [sushis.SUSHI, 1650, 70],
                  [sushis.SUSHI, 1750, 70],
                  [sushis.SUSHI, 1838, 70],
                  [sushis.SUSHI, 1770, 570],
                  [sushis.SUSHI, 1870, 570],
                  ]

        # Add sushi
        for sushi in point:
            food = sushis.Sushi(sushi[0])
            food.rect.x = sushi[1]
            food.rect.y = sushi[2]
            food.player = self.player
            self.sushi_list.add(food)


# Level Three
class Level_03(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("pink.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1400  # End of level

        # Array with all the platforms with the (x, y) coordinates
        level = [ [platforms.MYCELIUM_LEFT, 500, 500],
                  [platforms.BARRIER, 110, 0],
                  [platforms.MYCELIUM_MIDDLE, 539, 500],
                  [platforms.MYCELIUM_RIGHT, 576, 500],
                  [platforms.MYCELIUM_LEFT, 800, 350],
                  [platforms.MYCELIUM_MIDDLE, 839, 350],
                  [platforms.MYCELIUM_RIGHT, 876, 350],
                  [platforms.MYCELIUM_LEFT, 1000, 200],
                  [platforms.MYCELIUM_MIDDLE, 1039, 200],
                  [platforms.MYCELIUM_RIGHT, 1076, 200],
                  [platforms.VERTICAL_BARRIER, 300, 522],
                  [platforms.VERTICAL_BARRIER, 700, 522],
                  [platforms.VERTICAL_BARRIER, 1500, 522],
                  [platforms.VERTICAL_BARRIER, 1900, 522],
                  [platforms.MYCELIUM_LEFT, 1200, 150],
                  [platforms.MYCELIUM_MIDDLE, 1238, 150],
                  [platforms.MYCELIUM_MIDDLE, 1276, 150],
                  [platforms.MYCELIUM_MIDDLE, 1314, 150],
                  [platforms.MYCELIUM_MIDDLE, 1352, 150],
                  [platforms.MYCELIUM_MIDDLE, 1390, 150],
                  [platforms.MYCELIUM_MIDDLE, 1428, 150],
                  [platforms.MYCELIUM_MIDDLE, 1466, 150],
                  [platforms.MYCELIUM_MIDDLE, 1504, 150],
                  [platforms.MYCELIUM_MIDDLE, 1543, 150],
                  [platforms.MYCELIUM_MIDDLE, 1580, 150],
                  [platforms.MYCELIUM_RIGHT, 1618, 150],
                  [platforms.MYCELIUM_LEFT, 1238, 350],
                  [platforms.MYCELIUM_MIDDLE, 1276, 350],
                  [platforms.MYCELIUM_MIDDLE, 1314, 350],
                  [platforms.MYCELIUM_MIDDLE, 1352, 350],
                  [platforms.MYCELIUM_MIDDLE, 1390, 350],
                  [platforms.MYCELIUM_MIDDLE, 1428, 350],
                  [platforms.MYCELIUM_MIDDLE, 1466, 350],
                  [platforms.MYCELIUM_MIDDLE, 1504, 350],
                  [platforms.MYCELIUM_MIDDLE, 1543, 350],
                  [platforms.MYCELIUM_MIDDLE, 1580, 350],
                  [platforms.MYCELIUM_RIGHT, 1618, 350]
                  ]

        # Add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with all the sushi and coordinates for the sushi
        point = [ [sushis.SUSHI, 510, 470],
                  [sushis.SUSHI, 570, 470],
                  [sushis.SUSHI, 1150, 270],
                  [sushis.SUSHI, 1100, 300],
                  [sushis.SUSHI, 1300, 300],
                  [sushis.SUSHI, 1400, 300],
                  [sushis.SUSHI, 1500, 100],
                  [sushis.SUSHI, 2000, 200],
                  [sushis.SUSHI, 1650, 100],
                  [sushis.SUSHI, 1750, 300],
                  [sushis.SUSHI, 2100, 300],
                  [sushis.SUSHI, 1770, 300],
                  [sushis.SUSHI, 1870, 500],
                  [sushis.SUSHI, 1000, 470],
                  [sushis.SUSHI, 1050, 470],
                  [sushis.SUSHI, 1950, 570],
                  [sushis.SUSHI, 1950, 470],
                  [sushis.SUSHI, 1950, 200],
                  [sushis.SUSHI, 1250, 450],
                  [sushis.SUSHI, 1138, 100],
                  [sushis.SUSHI, 1210, 50],
                  [sushis.SUSHI, 1700, 400],
                  [sushis.SUSHI, 1290, 550],
                  [sushis.SUSHI, 1370, 570],
                  [sushis.SUSHI, 1470, 570]
                  ]

        # Add sushi
        for sushi in point:
            food = sushis.Sushi(sushi[0])
            food.rect.x = sushi[1]
            food.rect.y = sushi[2]
            food.player = self.player
            self.sushi_list.add(food)

# Level Four
class Level_04(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("oasis.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1600  # End of level

        # Array with all the platforms with the (x, y) coordinates
        level = [ [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1038, 500],
                  [platforms.GRASS_RIGHT, 1076, 500],
                  [platforms.BARRIER, 110, 0],
                  [platforms.GRASS_LEFT, 500, 450],
                  [platforms.GRASS_MIDDLE, 538, 450],
                  [platforms.GRASS_RIGHT, 576, 450],
                  [platforms.GRASS_LEFT, 1600, 400],
                  [platforms.GRASS_MIDDLE, 1638, 400],
                  [platforms.GRASS_RIGHT, 1676, 400],
                  [platforms.GRASS_LEFT, 1700, 200],
                  [platforms.GRASS_MIDDLE, 1738, 200],
                  [platforms.GRASS_RIGHT, 1776, 200],
                  [platforms.GRASS_LEFT, 2200, 500],
                  [platforms.GRASS_MIDDLE, 2238, 500],
                  [platforms.GRASS_RIGHT, 2276, 500],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.GRASS_MIDDLE, random.randrange(300, 2400), random.randrange(50, 570)],
                  [platforms.VERTICAL_BARRIER, random.randrange(300, 2400), random.randrange(50, 570)]
                  ]

        # Add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

# Level Five
class Level_05(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("snow.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1800  # End of level

        # Array with all the platforms with the (x, y) coordinates
        level = [ [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.MYCELIUM_MIDDLE, 1038, 500],
                  [platforms.GRASS_RIGHT, 1076, 500],
                  [platforms.BARRIER, 110, 0],
                  [platforms.GRASS_LEFT, 500, 450],
                  [platforms.MYCELIUM_MIDDLE, 538, 450],
                  [platforms.GRASS_RIGHT, 576, 450],
                  [platforms.GRASS_LEFT, 1600, 400],
                  [platforms.MYCELIUM_MIDDLE, 1638, 400],
                  [platforms.GRASS_RIGHT, 1676, 400],
                  [platforms.GRASS_LEFT, 1700, 200],
                  [platforms.MYCELIUM_MIDDLE, 1738, 200],
                  [platforms.GRASS_RIGHT, 1776, 200],
                  [platforms.GRASS_LEFT, 2200, 500],
                  [platforms.MYCELIUM_MIDDLE, 2238, 500],
                  [platforms.GRASS_RIGHT, 2276, 500],
                  [platforms.MYCELIUM_LEFT, 2238, 350],
                  [platforms.MYCELIUM_MIDDLE, 2276, 350],
                  [platforms.MYCELIUM_MIDDLE, 2314, 350],
                  [platforms.MYCELIUM_MIDDLE, 2352, 350],
                  [platforms.MYCELIUM_MIDDLE, 2390, 350],
                  [platforms.MYCELIUM_MIDDLE, 2428, 350],
                  [platforms.MYCELIUM_MIDDLE, 2466, 350],
                  [platforms.MYCELIUM_MIDDLE, 2504, 350],
                  [platforms.MYCELIUM_MIDDLE, 2543, 350],
                  [platforms.MYCELIUM_MIDDLE, 2580, 350],
                  [platforms.MYCELIUM_RIGHT, 2618, 350]
                  ]

        # Add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.MYCELIUM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



