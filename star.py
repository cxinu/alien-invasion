import pygame
import random


class Star(pygame.sprite.Sprite):
    """A single floating star in the background"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.Surface((2, 2))  # Small square star
        self.image.fill((255, 255, 255))  # White color
        self.rect = self.image.get_rect()

        # Start at a random position
        self.rect.x = random.randint(0, self.settings.screen_width)
        self.rect.y = random.randint(0, self.settings.screen_height)

        # Store vertical position as a float for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.star_speed
        self.rect.y = self.y

        # Reset to top when it goes off-screen
        if self.rect.top > self.settings.screen_height:
            self.rect.y = 0
            self.y = 0
            self.rect.x = random.randint(0, self.settings.screen_width)
