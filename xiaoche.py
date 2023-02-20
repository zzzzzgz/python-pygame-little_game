# coding=utf-8
import pygame
from pygame.locals import *
import sys
import random


class xiaoche(pygame.sprite.Sprite):
    def __init__(self,bgsize):
        pygame.sprite.Sprite.__init__(self)
        self.jishu = 1
        self.speed = 5
        self.active = True
        self.image1=pygame.image.load('image/xiaoche.png').convert_alpha()
        self.image2 = pygame.image.load('image/xiaoche2.png').convert_alpha()
        self.image3 = pygame.image.load('image/xiaoche3.png').convert_alpha()
        self.image4 = pygame.image.load('image/xiaoche4.png').convert_alpha()
        self.rect=self.image1.get_rect()
        self.width,self.height=bgsize[0],bgsize[1]
        self.rect.left=(self.width-self.rect.width)//2
        self.rect.top=(self.height-self.rect.height-5)
        self.zuo= self.rect.left
        self.you= self.rect.left+self.rect.width

    def moveleft(self):
        if self.rect.left>0:
            self.rect.left-=self.speed*self.jishu
        else:
            self.rect.left=0
    def moveright(self):
        if self.rect.right<self.width:
            self.rect.right+=self.speed*self.jishu
        else:
            self.rect.right = self.width

