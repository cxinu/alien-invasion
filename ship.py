import pygame


class Ship:
    """A class to manage the player's ship"""

    def __init__(self, ai_game):
        """Initializing the ship and set its starting position"""
        self.screen = ai_game.screen
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

    def update(self):
        """Update ships movement based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
