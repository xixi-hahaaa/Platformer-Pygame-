# Game Main Program

# Import a library of functions called 'pygame'
import pygame
import constants
import levels
import sys
from player import Player

# Main Program Loop
def main():
    # Initiate pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Bear Run")

    # Set up the player sprite class
    player = Player()

    # Levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))
    level_list.append(levels.Level_05(player))

    # Current level
    current_level_num = 0
    current_level = level_list[current_level_num]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 150   # CHANGE VALUE
    player.rect.y = constants.HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Initiate music mixer
    pygame.mixer.init()

    # Load background music file
    pygame.mixer.music.load("Symphony_No.6_Beethoven.ogg")

    # Play music
    pygame.mixer.music.play()

    # Select font, font size, bold, italics
    font = pygame.font.SysFont("Walkway", 50, False, True)
    final_font = pygame.font.SysFont("Walkway", 72, True, True)

    # Counter for when to switch to show final score
    run = 0

    # Mouse
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    # Load loop images
    start_img = pygame.image.load("start.png")
    rule_img = pygame.image.load("rules.png")
    end_img = pygame.image.load("end.png")

    # Loops
    done = False
    startloop = True
    ruleloop = False
    gameloop = False
    endloop = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Start Screen Loop -----------
    while startloop == True:
        for event in pygame.event.get(): # See what user wants to do
            if event.type == pygame.QUIT: # If user clicked exit button
                startloop = False
                ruleloop = False
                gameloop = False
                endloop = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Click to begin game
                startloop = False
                ruleloop = False
                gameloop = True
                endloop = False
            elif event.type == pygame.KEYDOWN:  # Press r to read rules
                if event.key == pygame.K_r:
                    startloop = False
                    ruleloop = True
                    gameloop = False
                    endloop = False 

        # Draw start screen
        screen.blit(start_img, (0, 0))

        # Display update
        pygame.display.update()

    # -------- Rule Program Loop -----------
    while ruleloop == True:
        for event in pygame.event.get(): # See what user wants to do
            if event.type == pygame.QUIT: # If user clicked exit button
                startloop = False
                ruleloop = False
                gameloop = False
                endloop = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Click to begin game
                startloop = False
                ruleloop = False
                gameloop = True
                endloop = False

        # Draw start screen
        screen.blit(rule_img, (0, 0))

        # Display update
        pygame.display.update()
            

    # -------- Game Program Loop -----------
    while gameloop == True:
        for event in pygame.event.get(): # Check to see what the user did
            if event.type == pygame.QUIT: # If user clicked exit button
                startloop = False
                ruleloop = False
                gameloop = False
                endloop = False
                pygame.quit()       # Quit game
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        
        # Render score image 
        text = font.render("score: " + str(player.score), True, constants.WHITE)   # gameloop

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            run += 1
            if current_level_num < len(level_list) - 1:
                current_level_num += 1
                current_level = level_list[current_level_num]
                player.level = current_level

        # Switch to endscreen 
        if run > 6:
            startloop = False
            ruleloop = False
            gameloop = False
            endloop = True

        # Draw levels, score, and sprites
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        screen.blit(text,[650, 100])

        # Limit to 60 frames per second
        clock.tick(60)

        # Update
        pygame.display.update()

    # -------- End Screen Loop -----------
    while endloop == True:
        for event in pygame.event.get(): # See what user wants to do
            if event.type == pygame.QUIT: # If user clicked exit button
                startloop = False
                ruleloop = False
                gameloop = False
                endloop = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    main()      # Restart the game and reset values
                    run = 0
                    player.score = 0

        # Render final score
        final_text = final_font.render(str(player.score), True, constants.WHITE)   # endloop

        # Draw end screen
        screen.blit(end_img, (0, 0))
        screen.blit(final_text, [350, 400])

        # Display update
        pygame.display.update()
        

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

