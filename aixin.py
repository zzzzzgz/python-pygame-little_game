import pygame
from random import *

class aixin(pygame.sprite.Sprite):
    def __init__(self, bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.beilv=1
        self.canshu = 1
        self.active = True
        self.image = pygame.image.load("image/aixing.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed = 10
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -5*self.height)
        self.zuo=self.rect.left
        self.you=self.rect.left+self.rect.width

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-20 * self.height, -10*self.height)
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed * self.canshu*self.beilv
        else:
            self.reset()

class danqi(pygame.sprite.Sprite):
    def __init__(self, bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.canshu = 1
        self.beilv = 1
        self.active = True
        self.image = pygame.image.load("image/n2o.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed = 8
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -5*self.height)
        self.zuo=self.rect.left
        self.you=self.rect.left+self.rect.width

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-2 * self.height, -1*self.height)
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed * self.canshu*self.beilv
        else:
            self.reset()

class life():
    def __init__(self, bgsize):
        self.shengming=5
        self.width, self.height = bgsize[0], bgsize[1]
        self.image = pygame.image.load("image/aixin.png").convert_alpha()
