import pygame
from pygame.sprite import Group

from game_settings import GameSettings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()

    game_settings = GameSettings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics and scoreboard
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    # Make the Play button
    play_button = Button(screen, 'Play')
    # Make a ship
    ship = Ship(game_settings, screen)

    # Make an alien
    aliens = Group()

    # Make a group to store bullets in
    bullets = Group()

    # Create the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Watch for keyboard and mouse events
    while True:
        gf.check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
