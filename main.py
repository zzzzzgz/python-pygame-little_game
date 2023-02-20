import pygame
import xiaoche
import sys
import traceback
import luzhang
import aixin
import sucai
import GAME
from pygame.locals import *
from random import *

black = (0, 0, 0)
white = (255, 255, 255)
yellow=(255,255,0)
red=(255,0,0)
skyblue=(240,255,255)
blue=(0,0,255)

pygame.init()
pygame.mixer.init()

bgsize = width,height =500,900
screen = pygame.display.set_mode(bgsize)
pygame.display.set_caption('�?虾户')
background1 = pygame.image.load('image/lu1.png').convert()
background2 = pygame.image.load('image/lu2.png').convert()

#载入音效
pygame.mixer.music.load("music/bgmusic.mp3")
pygame.mixer.music.set_volume(0.1)
wangwang=pygame.mixer.Sound("music/wang.wav")
wangwang.set_volume(0.2)
bkla=pygame.mixer.Sound("music/bkla.wav")
bkla.set_volume(0.5)
pu=pygame.mixer.Sound("music/pu.wav")
pu.set_volume(0.9)
dqhf=pygame.mixer.Sound("music/dq.wav")
dqhf.set_volume(0.2)
smhf=pygame.mixer.Sound("music/sm.wav")
smhf.set_volume(0.2)
sl=pygame.mixer.Sound("music/shenglang.wav")
sl.set_volume(0.1)

def add_ren(group1,group2,num):
    for i in range(num):
        r1=luzhang.ren(bgsize)
        group1.add(r1)
        group2.add(r1)

def add_gou(group1,group2,num):
    for i in range(num):
        r1=luzhang.gou(bgsize)
        group1.add(r1)
        group2.add(r1)

def add_bb(group1,group2,num):
    for i in range(num):
        r1=luzhang.bb(bgsize)
        group1.add(r1)
        group2.add(r1)

def add_xjp(group1,group2,num):
    for i in range(num):
        r1=luzhang.xjp(bgsize)
        group1.add(r1)
        group2.add(r1)

def add_ax(group1,group2,num):
    for i in range(num):
        r1=aixin.aixin(bgsize)
        group1.add(r1)
        group2.add(r1)

def add_dq(group1,group2,num):
    for i in range(num):
        r1=aixin.danqi(bgsize)
        group1.add(r1)
        group2.add(r1)


def main():
    pygame.mixer.music.play(-1)
    sucai1=sucai.sucai(bgsize)
    mxiaoche = xiaoche.xiaoche(bgsize)
    gamover = GAME.over()
    shengming=aixin.life(bgsize)
    highscore=False



    luzhangs=pygame.sprite.Group()
    haodx = pygame.sprite.Group()

    xjp = pygame.sprite.Group()
    add_xjp(xjp, luzhangs, 2)

    bb=pygame.sprite.Group()
    add_bb(bb,luzhangs,2)

    ren=pygame.sprite.Group()
    add_ren(ren,luzhangs,4)

    gou=pygame.sprite.Group()
    add_gou(gou,luzhangs,3)

    axs=pygame.sprite.Group()
    add_ax(axs,haodx,1)

    dqs=pygame.sprite.Group()
    add_dq(dqs,haodx,1)

    clock = pygame.time.Clock()

    #各�?�参�?

    switch_image = True
    super=False
    delay = 100
    jsxianshi=True
    danqi=0
    life=3
    score=0
    score_font=pygame.font.Font("font/�?墨钧�?.ttf",20)

    running =True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  # 当按下关�?按键
                pygame.quit()
                sys.exit()  # 接收到退出事件后退出程�?
        key_pressed =pygame.key.get_pressed()

        if switch_image:
            screen.blit(background1, (0, 0))
        else:
            screen.blit(background2, (0, 0))

        if score < 10000:
            stancol = white
            stan = 1
        if score >= 10000 and score < 20000:
            stancol = black
            stan = 2
        if score >= 20000:
            stancol = red
            stan = 3

        if stan==1:
            for each in luzhangs:
                each.beilv = 1
            for each in haodx:
                each.beilv = 1
        if stan==2:
            for each in luzhangs:
                each.beilv = 1.5
            for each in haodx:
                each.beilv = 1.5
        if stan==3:
            for each in luzhangs:
                each.beilv = 2
            for each in haodx:
                each.beilv = 2

        if life > 0:
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                mxiaoche.moveleft()

            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                mxiaoche.moveright()

            #挂挡了！
            if key_pressed[K_1]:
                for each in gou:
                    each.jishu=1
                for each in bb:
                    each.jishu=1
                for each in xjp:
                    each.jishu = 1
                for each in ren:
                    each.jishu=1
                for each in haodx:
                    each.canshu=1
                mxiaoche.jishu = 1

            if key_pressed[K_2]:
                for each in bb:
                    each.jishu=2
                for each in xjp:
                    each.jishu =2
                for each in gou:
                    each.jishu=2
                for each in ren:
                    each.jishu=2
                for each in haodx:
                    each.canshu = 2
                mxiaoche.jishu= 2

            if key_pressed[K_3]:
                for each in bb:
                    each.jishu=3
                for each in xjp:
                    each.jishu =3
                for each in gou:
                    each.jishu = 3
                for each in ren:
                    each.jishu = 3
                for each in haodx:
                    each.canshu = 2
                mxiaoche.jishu = 2

            if key_pressed[K_w]:
                if danqi<100:
                    danqi+=0.2
                    super=True
                    sl.play()
                    for each in bb:
                        each.jishu = 5
                    for each in xjp:
                        each.jishu = 5
                    for each in gou:
                        each.jishu = 5
                    for each in ren:
                        each.jishu = 5
                    for each in haodx:
                        each.canshu = 5
                    mxiaoche.jishu = 4
                else:
                    super=False
                    for each in bb:
                        each.jishu = 3
                    for each in xjp:
                        each.jishu = 3
                    for each in gou:
                        each.jishu = 3
                    for each in ren:
                        each.jishu = 3
                    for each in haodx:
                        each.canshu = 3
                    mxiaoche.jishu = 2
            else:
                if  mxiaoche.jishu == 4:
                    super=False
                    for each in bb:
                        each.jishu = 3
                    for each in xjp:
                        each.jishu = 3
                    for each in gou:
                        each.jishu = 3
                    for each in ren:
                        each.jishu = 3
                    for each in haodx:
                        each.canshu = 3
                    mxiaoche.jishu = 2

            if super == False:
                score += 1
            else:
                score += 10



        #利用帧数变化改变图像
        delay-=1
        if not delay:
            delay =100
        if not (delay%5):
            switch_image=not switch_image

        if score>=5000:
            jsxianshi=False

        pdluzhang = pygame.sprite.spritecollide(mxiaoche,luzhangs,False)
        if pdluzhang:
            if pygame.sprite.spritecollide(mxiaoche,xjp,False):
                ran1=randint(0,1)
                for e in pdluzhang:
                    e.active = False
                    pu.play()
                if ran1==0:
                    if  mxiaoche.rect.left+80<bgsize[0]:
                        mxiaoche.rect.left+=80
                    else:
                        mxiaoche.rect.left=bgsize[0]
                else:
                    if mxiaoche.rect.left -80 > 0:
                        mxiaoche.rect.left -= 80
                    else:
                        mxiaoche.rect.left=0

            else:
                life-=1
                for e in pdluzhang:
                        e.active=False
                if pygame.sprite.spritecollide(mxiaoche,gou,False):
                    wangwang.play()
                if pygame.sprite.spritecollide(mxiaoche, ren, False):
                    bkla.play()
                if pygame.sprite.spritecollide(mxiaoche,bb,False):
                    pu.play()

        pdax = pygame.sprite.spritecollide(mxiaoche,axs,False)
        if pdax:
            score += 1000
            if life<=4:
                life+=1
            for u in pdax:
                smhf.play()
                u.active = False

        pddq = pygame.sprite.spritecollide(mxiaoche,dqs,False)
        if pddq:
            danqi=0
            score+=500
            for u in pddq:
                dqhf.play()
                u.active = False


            #绘制我方小车
        if switch_image:
            if super==False:
                screen.blit(mxiaoche.image1,mxiaoche.rect)
            else:
                screen.blit(mxiaoche.image3, mxiaoche.rect)
        else:
            if super == False:
                screen.blit(mxiaoche.image2,mxiaoche.rect)
            else:
                screen.blit(mxiaoche.image4, mxiaoche.rect)

            #绘制障�?�物
        for each in gou:
                if each.active:
                    each.move()
                    if switch_image:
                        screen.blit(each.image1,each.rect)
                    else:
                        screen.blit(each.image2,each.rect)
                else:
                    each.reset()


        for each in bb:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    each.reset()


        for each in xjp:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    each.reset()

        for each in ren:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    each.reset()

            #绘制爱心和�?�条和�?气等�?
        for each in axs:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()

        for each in dqs:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()


        for i in range(life):
            screen.blit(shengming.image, (5+20*i,55))





        screen.blit(sucai1.shengming,sucai1.rect1)
        screen.blit(sucai1.danqi, sucai1.rect2)
        pygame.draw.rect(screen, (233,0,233), ((5,bgsize[1]-105),(20,105)))
        pygame.draw.rect(screen, (233, 255, 255), ((10, bgsize[1] - 100+danqi), (10, 100)))

        score_text = score_font.render("难度 : %s" % str(stan), True, stancol)
        screen.blit(score_text, (350, 55))

        score_text=score_font.render("SCORE : %s" % str(score),True,white)
        screen.blit(score_text,(320,25))
        if jsxianshi==True:
            js1=score_font.render("操作介绍�?" ,True,blue)
            screen.blit(js1,(10,75))
            js2=score_font.render("ad或左右键控制小车" ,True,yellow)
            screen.blit(js2,(10,100))
            js2=score_font.render("1�?2�?3�?�?换挡" ,True,black)
            screen.blit(js2,(10,125))
            js2=score_font.render("w�?使用�?�?" ,True,skyblue)
            screen.blit(js2,(10,150))


        if life==0:
            GAME.over()
            for each in luzhangs:
                each.reset()
                each.active=False
                each.jishu=0
            for each in haodx:
                each.reset()
                each.active=False
                each.canshu=0
                text_font = pygame.font.Font("font/�?墨钧�?.ttf", 40)
            end_text = text_font.render("您的最终得分为 : %s" % str(score), True,yellow)
            end_text1 = text_font.render("按空格键重新开�?", True, black)
            with open("record.txt","r") as f:
                record_socre=int(f.read())
                end_text2 = text_font.render("历史最高分�? : %s" % str(record_socre), True, yellow)
            if score>record_socre:
                highscore=True
                end_text3 = text_font.render("�?喜！您打破了历史最高分!", True, yellow)

                with open("record.txt","w") as f:
                    f.write(str(score))

            screen.blit(end_text, (50, 225))
            screen.blit(end_text1, (70, 625))
            screen.blit(end_text2, (50, 125))
            if highscore==True:
                screen.blit(end_text3, (10, 325))
            if switch_image:
                screen.blit(gamover.image1, (0,0))
            else:
                screen.blit(gamover.image2, (0,0))
            if key_pressed[K_SPACE]:
                main()


        pygame.display.flip()


        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()