import settings


class Bonus:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def move(self):
        pass

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))


class Heart(Bonus):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = settings.HEART
    
    def move(self):
        self.y += settings.HEART_SPEED
