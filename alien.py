import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.rect import Rect

class Alien(Sprite):
    """A class to represent an alien spaceship"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image: Surface = pygame.image.load("assets/alien.png")
        self.rect: Rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x: float = float(self.rect.x)

    def check_edges(self) -> bool:
        """Return true if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self) -> None:
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
