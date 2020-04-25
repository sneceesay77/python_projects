import pygame


class Rocket:
    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()
        self.image = pygame.image.load(
            '/home/sc306/Dropbox/SA/LearningPython/coding/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        """Draw a ship at the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.rocket_speed
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.rocket_speed
        if self.moving_up:
            if self.moving_up and self.rect.top > 0:
                self.y -= self.settings.rocket_speed
        if self.moving_down:
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y
