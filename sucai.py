import pygame

class sucai():
    def __init__(self, bgsize):
        self.width, self.height = bgsize[0], bgsize[1]
        self.shengming = pygame.image.load("image/20life.png").convert_alpha()
        self.danqi = pygame.image.load("image/50dq.png").convert_alpha()
        self.rect1 = self.shengming.get_rect()
        self.rect1.left = 5
        self.rect1.top = 5
        self.rect2 = self.danqi.get_rect()
        self.rect2.left = 5
        self.rect2.top = bgsize[1]-140.