
import pygame as pg
#from Characters import Members

import math  
  
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
  
# 定义窗口的分辨率
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

# 定义画面帧率
FRAME_RATE = 30
# 定义动画周期（帧数）

offset = {pg.K_LEFT:0, pg.K_RIGHT:0, pg.K_UP:0, pg.K_DOWN:0}

clock = pg.time.Clock()

def GameInit():
    #初始化游戏
    pg.init()
    pg.display.set_caption("MyVoiceIsNotLittle")
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    background = pg.image.load("Textrue/GameBackground.png")
    screen.blit(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


    #角色加载

    #创建花谱，情绪



def GameStart():

    distrubed_flag = False


    GameInit()



    running = True

    while running:

        #控制游戏的最大帧率
        clock.tick(FRAME_RATE)


        #进入大循环，当输了才会退出


        #if():
        #    distrubed_flag = True
        #else:
        #    distrubed_flag = False

        #当按下说话键时
        #if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: 
            #花谱的体力减少

         #   Flower.Power = Flower.Power-1
            #如果受到妨碍时则不会传输到
          #  if(): 
           #     senteme -1

            #当体力用完时就代表游戏结束
            #if(1):
             #   running = False

            #当想表达的话说完时则代表游戏结束

            #if(1):
             #   running = False

    pg.quit()

