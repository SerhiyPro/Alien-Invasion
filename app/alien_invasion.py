import sys
import pygame


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color
    bg_color = (230, 230, 230)

    # Watch for keyboard and mouse events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(bg_color)

        # Make the most recently drawn screen visible (hide old elements and shows new)
        pygame.display.flip()


run_game()
