import pygame

from zh_08_plane_sprites import *
pygame.init()

#set_mode(resultion=(0,0),flags=0,deph=0)-->Surface
screen=pygame.display.set_mode((480,700))

#绘制背景图像

# load  加载图像数据
background=pygame.image.load("./images/background.png")
#blit  绘制图像
screen.blit(background,(0,0))
# update 更新屏幕显示
pygame.display.update()

hero=pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
pygame.display.update()
clock=pygame.time.Clock()
hero_rect=pygame.Rect(200,500,102,126)

enemy=GameSprite("./images/enemy1.png")
enemy1=GameSprite("./images/enemy2.png",2)
enemy_group=pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)

                # #监听事件
                #     event_list=pygame.event.get()
                #     if len(event_list)>0:
                #         print(event_list)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('游戏退出')

            pygame.quit()
            #终止当前正在执行的
            exit()

    hero_rect.y-=1
    if hero_rect.y<=-126:
        hero_rect.y=700
    screen.blit(background,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()

    enemy_group.draw(screen)
    pygame.display.update()




pygame.quit()

