# -*- coding = utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
import math
from random import randint
from Characters import Members


def calculate_distance(x1, y1, x2, y2):  
    """  
    计算两点之间的距离。  
  
    参数:  
    x1, y1 (float): 第一个点的坐标。  
    x2, y2 (float): 第二个点的坐标。  
  
    返回:  
    float: 两点之间的距离。  
    """  
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  
    return distance  


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)

pygame.init()


font = pygame.font.SysFont('SimHei', 36)
pygame.display.set_caption("MyVoiceIsNotLittle")
clock = pygame.time.Clock()



screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])



background = pygame.image.load("Textrue/GameBackground.png")

screen.blit(background, (0, 0))


Flower_single = Members.Flower()
sentiment_single = Members.sentiment()
Mei_single = Members.Mei()

distrubed_Flag = False


while True:
    #进行关闭等操作
    if((calculate_distance(Flower_single.rect.top,Flower_single.rect.left,Mei_single.rect.top,Mei_single.rect.left)/10<27)):
        distrubed_Flag = True
    else:
        distrubed_Flag = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            Flower_single.Power -= 1
            if(not distrubed_Flag):
                Flower_single.express -= 1


    #绘制花谱在桌面上
    screen.blit(background, (0, 0))
    screen.blit(Flower_single.image, Flower_single.rect)
    screen.blit(sentiment_single.image, sentiment_single.rect)

    Mei_single.update()
    screen.blit(Mei_single.image, Mei_single.rect)
    score_text = font.render(f"hua's power is {Flower_single.Power}, the lest expression os {Flower_single.express}", True, WHITE)
    screen.blit(score_text, (10, 10))
    if(Flower_single.express <= 0):
        win_score_text = font.render("you win", True, WHITE)
        screen.blit(win_score_text, (20, 20))

    if(Flower_single.Power <= 0):
        loss_score_text = font.render("you loss", True, WHITE)
        screen.blit(loss_score_text, (20, 20))

    pygame.display.update()

