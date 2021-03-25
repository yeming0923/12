import pygame
from zh_08_plane_sprites import *

class PlaneGame(object):

    def __init__(self):

        print("游戏初始化")
        # 1.创建游戏窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock=pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self._creat_sprites()

    def _creat_sprites(self):
        bg1=Background()
        bg2=Background(is_alt=1)


        self.back_group=pygame.sprite.Group(bg1,bg2)




    def start_game(self):
        print("游戏开始...")

        while True:

            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self._event_handler()
            # 3.碰撞检测
            self._check_collide()
            # 4.更新绘制精灵组
            self._update_sprites()
            # 5.更新检测
            pygame.display.update()

    def _event_handler(self):

        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type==pygame.QUIT:
                PlaneGame._game_over()

    def _check_collide(self):
        pass
    def _update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)



    @staticmethod
    def _game_over(self):
        print("游戏结束...")

        pygame.quit()
        exit()



if __name__ == '__main__':
    #创建游戏对象
    game=PlaneGame()
    #启动游戏
    game.start_game()