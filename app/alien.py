import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, game_settings, screen):
        """Initialize the alien and set it starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.game_settings.alien_speed_factor *
                   self.game_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)
