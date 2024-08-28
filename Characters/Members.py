import os
import random
from typing import List

import pygame as pg

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700


#调整图像大小
scaled_width = 100
scaled_height = 100

Flower_initial_position = (400,240)

sentiment_initial_position = (480,240)

Mei_initial_position = (40,40)

class Flower(pg.sprite.Sprite):
    #设置说话量与力气

    Power = 80

    express = 30

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Textrue/花.png")
        scaled_image = pg.transform.scale(self.image, (scaled_width, scaled_height))
        self.image = scaled_image
        #self.rect  = self.image.get_rect() #设置图片的大小
        self.rect = self.image.get_rect().inflate(10,10)
        self.rect.topleft = Flower_initial_position

    def Speak(self,distrubed_flag:bool):
        self.Power -= 1
        if(not (distrubed_flag)):
            self.express -= self.express



## 定义异世界情绪

class sentiment(pg.sprite.Sprite):

    #设定为站在花谱对面，什么都不干，只是个背景版

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Textrue/情.png")
        scaled_image = pg.transform.scale(self.image, (scaled_width, scaled_height))
        self.image = scaled_image
        #self.rect  = self.image.get_rect() #设置图片的大小
        self.rect = self.image.get_rect().inflate(10,10)
        self.rect.topleft = sentiment_initial_position


class Mei(pg.sprite.Sprite):
    #设定为在屏幕处乱走，会在塔范围内说话会被打断

    Power = 30
    Posixion_x = 0
    Posixion_y = 0
    X_speed = 3
    Y_speed = 3

    express = 50

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Textrue/芽.png")
        scaled_image = pg.transform.scale(self.image, (scaled_width, scaled_height))
        self.image = scaled_image
        #self.rect  = self.image.get_rect() #设置图片的大小
        self.rect = self.image.get_rect().inflate(10,10)
        self.rect.topleft = Mei_initial_position


    #每一次更新位置

    def update(self):

        if(self.rect.left >= SCREEN_WIDTH or self.rect.left <= 0):
            self.X_speed = -self.X_speed

        if(self.rect.top >= SCREEN_HEIGHT or self.rect.top <= 0):
            self.Y_speed = -self.Y_speed


        # 对位置的方式想个办法
        self.rect.left += self.X_speed
        self.rect.top += self.Y_speed


#定义春缘火


class Flame(pg.sprite.Sprite):
    #设定为在桌面上随机出现，当出现3后会拿出喇叭，有时说话会被打扰


    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Textrue/春.png")
        scaled_image = pg.transform.scale(self.image, (scaled_width, scaled_height))
        self.image = scaled_image
        #self.rect  = self.image.get_rect() #设置图片的大小
        self.rect = self.image.get_rect().inflate(10,10)
        self.rect.topleft = Mei_initial_position

    # 出现后会在30秒后拿出喇叭，并播放一会 
    def ShowUp(self):
        pass

