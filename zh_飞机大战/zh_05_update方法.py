import pygame

pygame.init()

#set_mode(resultion=(0,0),flags=0,deph=0)-->Surface
screen=pygame.display.set_mode((480,700))

background=pygame.image.load("./images/background.png")
screen.blit(background,(0,0))
#pygame.display.update()

hero=pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
#update 方法可以最后统一显示
pygame.display.update()

while True:
    pass

pygame.quit()

