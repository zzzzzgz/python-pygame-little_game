import pygame


class over():
    def __init__(self):
        self.image1 = pygame.image.load("image/gameover.png").convert_alpha()
        self.image2 = pygame.image.load("image/gameover2.png").convert_alpha()
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
