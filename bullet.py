import settings


class AbstractBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = None
        
    def move(self):
        self.y -= settings.BULLET_SPEED

    def draw(self, window):
        window.blit(self.bullets, (self.x, self.y))


class Laser(AbstractBullet):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.bullets = settings.YELLOW_LASER
