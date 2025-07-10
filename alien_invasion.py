import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage alien invasion"""

    def __init__(self):
        """Initializing the game and creating the game resources"""
        pygame.init()
        # For consistent frame rate a clock is made.
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            """
            Check for keyboard and mouse events
            event.get returns a list of all the events that are currently in the event queue.
            """
            self._check_events()
            self._update_screen()
            self.ship.update()
            """Make the most recently drawn screen visible"""
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and events"""
        """
        get() collects and returns a list of Event objects currently in the event queue.
        Each item in that list is an instance of Pygame's Event class
        event is one Event object
        event.type is an attribute on that Event object telling you what kind of event it is.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    """Move ship to the right"""
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
