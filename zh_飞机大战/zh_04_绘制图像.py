import pygame

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


while True:
    pass

pygame.quit()

