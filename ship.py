import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the player's ship"""

    def __init__(self, ai_game):
        """Initializing the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = (
            ai_game.screen.get_rect()
        )  # Store the dimensions of screen so we can place ship correctly
        """Start the ship with no movement, movement flag."""
        self.moving_right = False
        self.moving_left = False
        """Load the ship image and get its rect"""
        self.image = pygame.image.load("../alien-invasion/assets/player-ship.bmp")
        self.rect = self.image.get_rect()

        """Start each new ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def update(self):
        """Update ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
