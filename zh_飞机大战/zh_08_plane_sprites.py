import pygame
SCREEN_RECT=pygame.Rect(0,0,480,700)

#刷新的帧率
FRAME_PER_SEC=60

#创建
class GameSprite(pygame.sprite.Sprite):


    def __init__(self,image_name,speed=1):

        super().__init__()
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed

    def update(self):

        self.rect.y+=self.speed

class Background(GameSprite):
    def __init__(self,is_alt=False):
        # 1.调用父类方法实现精灵的创建（images/rect/speed）
        super().__init__("./images/background.png")
        #2.判断是否交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y=-self.rect.height

    def update(self):
        #1.调用父类方法实现
        super().update()
        #2.判断是否移出屏幕
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height

