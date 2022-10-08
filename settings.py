import pygame

class Settings:

    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        self.ship_speed = 2
        self.ship_limit = 3

        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.max_stars = 50
        self.star1 = pygame.image.load('./images/star.bmp')
        self.star2 = pygame.image.load('./images/star2.bmp')
        self.star3 = pygame.image.load('./images/star3.bmp')
        self.star_list = [self.star1, self.star2, self.star3]
        self.star_speed = 1

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 is right; -1 is left
