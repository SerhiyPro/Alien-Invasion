import sys
import pygame
import time

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        ship.shooting = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        ship.shooting = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Create a new bullet and add it to the bullets group"""
    if not bullets.sprites() or (time.time() - bullets.sprites()[-1].time) >= 0.1:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Update position of bullets and get rid of all bullets"""
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """
    Create a full flit of aliens
    Create an alien and find the number of aliens in a row
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = available_space_x // (2 * alien_width)

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, ship,  aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    if ship.shooting:
        fire_bullet(ai_settings, screen, ship, bullets)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible (hide old elements and shows new)
    pygame.display.flip()
