import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.rect import Rect


class Ship(Sprite):
    """A class to manage the player's ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position"""
        super().__init__()

        self.screen: Surface = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect: Rect = self.screen.get_rect()

        # Movement flags
        self.moving_right: bool = False
        self.moving_left: bool = False

        # Load the ship image and get its rect
        self.image: Surface = pygame.image.load("assets/player-ship.png")
        self.rect: Rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's horizontal position
        self.x: float = float(self.rect.x)

    def update(self) -> None:
        """Update ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)

    def blitme(self) -> None:
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
