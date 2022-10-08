from pygame.sprite import Sprite

class Stars(Sprite):

    def __init__(self, ai_game, star_sprite, sprite_num):

        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.image = star_sprite
        self.sprite_num = sprite_num
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.settings.star_speed
        self.rect.y = self.y
    
    def draw_star(self):
        self.screen.blit(self.image, self.rect)