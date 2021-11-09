from settings import *


class AbstractBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = None

    def move(self, velocity):
        self.y -= velocity

    def draw(self, window):
        window.blit(self.bullets, (self.x, self.y))


class Laser(AbstractBullet):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.bullets = YELLOW_LASER
