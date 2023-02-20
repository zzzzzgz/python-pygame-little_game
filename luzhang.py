import pygame
from random import *


class ren(pygame.sprite.Sprite):
    def __init__(self,bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.jishu = 1
        self.beilv = 1
        self.active = True
        self.image = pygame.image.load("image/reng.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed=2
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.top=randint(-4*self.height,0)

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-4 * self.height, 0)
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top+=self.speed * self.jishu*self.beilv
        else:
            self.reset()


class gou(pygame.sprite.Sprite):
    def __init__(self, bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.jishu = 1
        self.beilv = 1
        self.active = True
        self.image1 = pygame.image.load("image/xiaogou.png").convert_alpha()
        self.image2 = pygame.image.load("image/xiaogou2.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed = 5
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -self.height)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed * self.jishu*self.beilv
        else:
            self.reset()

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -self.height)
        self.active=True


class bb(pygame.sprite.Sprite):
    def __init__(self,bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.jishu = 1
        self.beilv = 1
        self.active = True
        self.image = pygame.image.load("image/bb.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed=1
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.top=randint(-8*self.height,0)

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-7 * self.height, 0)
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top+=self.speed * self.jishu*self.beilv
        else:
            self.reset()

class xjp(pygame.sprite.Sprite):
    def __init__(self,bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.jishu = 1
        self.beilv = 1
        self.active = True
        self.image = pygame.image.load("image/xjp.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.width, self.height = bgsize[0], bgsize[1]
        self.speed=3
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.top=randint(-4*self.height,0)

    def reset(self):
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-4 * self.height, 0)
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top+=self.speed * self.jishu*self.beilv
        else:
            self.reset()


