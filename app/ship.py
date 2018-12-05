import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, game_settings, screen):
        """Initializing the ship and setting its starting position"""
        super(Ship, self).__init__()

        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Position each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Used for continious shooting
        self.shooting = False

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship and its current location"""
        self.screen.blit(self.image, self.rect)
