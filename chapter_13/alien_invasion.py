import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group of aliens.
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
