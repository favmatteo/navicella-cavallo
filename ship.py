import settings

"""Classe astratta che rappresenta una navicella"""


class Ship:

    def __init__(self, x, y):
        """ Inizializza gli attributi della classe Ship """
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


""" Classe Player che eredita dalla classe Ship"""


class PlayerShip(Ship):

    def __init__(self, x, y):
        """ Inizializza gli attributi della classe PlayerShip """
        super().__init__(x, y)
        self.cool_down_counter = 0
        self.ship_img = settings.YELLOW_SPACE_SHIP


"""Classe Nemico"""


class EnemyShip(Ship):

    def __init__(self, x, y, color):
        """ Inizializza gli attributi della classe EnemyShip """
        super().__init__(x, y)
        self.colors = {
            "red": settings.RED_SPACE_SHIP,
            "green": settings.GREEN_SPACE_SHIP,
            "blue": settings.BLUE_SPACE_SHIP,
        }
        self.ship_img = self.colors.get(color, self.colors[
            'red'])

    def move(self):
        self.y += settings.ENEMY_SPEED
