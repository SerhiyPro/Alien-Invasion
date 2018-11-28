import pygame


class Ship:

    def __init__(self, screen):
        """Initializing the ship and setting its starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Position each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship and its current location"""
        self.screen.blit(self.image, self.rect)
