""" Classe che si occupa di controllare il funzionamento del gioco
    Muovere i personaggi, sparare, ecc """

import random
import ship
import bullet
import bonus
import settings

""" Classe che si occupa di controllare il funzionamento del gioco
    Disegnare su schermo, muovere i personaggi, sparare, ecc.. """


class Control:

    def __init__(self):
        """Inizializzazione attributi classe Control"""
        self.run = True
        self.level = 0
        self.lives = settings.INITIAL_LIVES
        self.kill = 0
        self.lost = False
        self.lost_count = 0
        self.clock = settings.pygame.time.Clock()
        self.player = ship.PlayerShip(settings.WIDTH / 2, settings.HEIGHT - 100)
        self.enemies = []
        self.bullets = []
        self.heart_cool_down = 0
        self.wave_length = 0
        self.hearts = []

    def update_window(self):
        """Metodo che si occupa di aggiornare la finestra"""

        # Disegna lo sfondo
        settings.WIN.blit(settings.BG, (0, 0))

        # Disegna le etichette
        lives_label = settings.MAIN_FONT.render(f"Vite: {self.lives}", 1, (0, 255, 0))
        level_label = settings.MAIN_FONT.render(f"Livello: {self.level}", 1, (0, 255, 0))
        lost_label = settings.MAIN_FONT.render(f"Hai perso!", 1, (0, 255, 0))
        kill_label = settings.MAIN_FONT.render(f"Uccisioni: {self.kill}", 1, (0, 255, 0))
        n_enemies = settings.MAIN_FONT.render(f"Nemici: {len(self.enemies)}", 1, (0, 255, 0))

        settings.WIN.blit(lives_label, (round(10), round(10)))
        settings.WIN.blit(level_label, (round(settings.WIDTH - level_label.get_width() - 10), round(10)))
        settings.WIN.blit(kill_label, (round(settings.WIDTH - kill_label.get_width() - 10), round(50)))
        settings.WIN.blit(n_enemies, (round(settings.WIDTH - n_enemies.get_width() - 10), round(90)))

        # Disegna ogni nemico
        for en in self.enemies:
            en.draw(settings.WIN)

        # Disegna ogni proiettile
        for blt in self.bullets:
            blt.draw(settings.WIN)

        # Disegna ogni cuore
        for heart in self.hearts:
            heart.draw(settings.WIN)

        # Se hai perso, te lo comunica
        if self.lost:
            settings.WIN.blit(lost_label, (round(settings.WIDTH / 2 - level_label.get_width() / 2), round(350)))

        # Disegna la navicella del giocatore
        self.player.draw(settings.WIN)

        # aggiorna lo schermo
        settings.pygame.display.update()

    def is_dead(self):
        """Metodo che controlla se il giocatore è morto"""
        if self.lives <= 0:
            self.lost = True

    def has_lost(self):
        """Metodo che controlla se il giocatore ha perso"""
        if self.lost:
            self.lost_count += 1
            self.player.x = settings.WIDTH / 2
            self.player.y = settings.HEIGHT - 100
            if self.lost_count >= settings.FPS * 5:
                self.lost = False

            if not self.lost:
                self.lives = settings.INITIAL_LIVES
                self.level = 0
                self.kill = 0
                self.wave_length = 0
                self.bullets = []
                self.enemies = []
                self.hearts = []
                self.lost_count = 0

            # rimuove tutti i nemici
            for en in self.enemies:
                self.enemies.remove(en)

            # rimuove tutti i cuori
            for heart in self.hearts:
                self.hearts.remove(heart)

    def are_enemies_death(self):
        """Metodo che controlla se tutti i nemici sono morti"""
        # Se sono morti tutti i nemici
        if len(self.enemies) == 0:
            if self.lives > 0:
                self.level += 1
                self.wave_length += 5
                for i in range(self.wave_length):
                    enemy = ship.EnemyShip(random.randint(70, settings.WIDTH - 100), random.randint(-1500, -100),
                                           random.choice(("red", "green", "blue")))
                    self.enemies.append(enemy)

    def quit_application(self):
        """Metodo che chiuda la finestra di pygame se si preme la X in alto a destra della finestra"""
        for event in settings.pygame.event.get():
            if event.type == settings.pygame.QUIT:
                self.run = False

    def pressed_key(self):
        """Metodo che rileva gli input da tastiera ed esegue determinate operazioni in base ad esso"""
        keys = settings.pygame.key.get_pressed()

        # Movimenti:
        # Destra
        if ((keys[settings.pygame.K_RIGHT] or keys[settings.pygame.K_d])
                and self.player.x + self.player.get_width() + settings.PLAYER_SPEED < settings.WIDTH) and not self.lost:
            self.player.x += settings.PLAYER_SPEED

        # Sinistra
        if ((keys[settings.pygame.K_LEFT] or keys[
                settings.pygame.K_a]) and self.player.x - settings.PLAYER_SPEED > 0) and not self.lost:
            self.player.x -= settings.PLAYER_SPEED

        # Su
        if ((keys[settings.pygame.K_UP] or keys[
                settings.pygame.K_w]) and self.player.y - settings.PLAYER_SPEED > 0) and not self.lost:
            self.player.y -= settings.PLAYER_SPEED

        # Giù
        if ((keys[settings.pygame.K_DOWN] or keys[settings.pygame.K_s])
                and self.player.y + self.player.get_height() + settings.PLAYER_SPEED < settings.HEIGHT) \
                and not self.lost:
            self.player.y += settings.PLAYER_SPEED

        # Se viene premuto il tasto spazio, e il cool down per sparare è <= 0 allora spara un laser
        if keys[settings.pygame.K_SPACE] and not self.lost:
            if self.player.cool_down_counter <= 0:
                # un proiettile ogni poco più di un secondo secondo 1.15 secondi
                self.player.cool_down_counter = settings.FPS / 2 * settings.BULLET_COOL_DOWN
                blt = bullet.Laser(self.player.x, self.player.y)
                self.bullets.append(blt)

    def move(self):
        """Metodo che si occupa di muovere ogni oggetto"""
        for en in self.enemies:
            en.move(settings.ENEMY_SPEED)
        for blt in self.bullets:
            blt.move(settings.BULLET_SPEED)
        for heart in self.hearts:
            heart.move(settings.HEART_SPEED)
        self.player.cool_down_counter -= 1
        self.heart_cool_down -= 1

    def collision_detector(self):
        """Metodo che si occupa di verificare varie collisioni tra gli oggetti"""
        for en in self.enemies:

            # Controlla se i nemici collidono con il giocatore
            if -50 < (en.y - self.player.y) < 50 and -50 < (en.x - self.player.x) < 50:
                self.lives -= 1
                self.enemies.remove(en)
                self.kill += 1

            # Controlla se i nemici escono dal bordo inferiore
            if en.y >= settings.HEIGHT:
                self.enemies.remove(en)
                self.lives -= 1

        for blt in self.bullets:
            for en in self.enemies:
                # Controlla se il proiettile colpisce un nemico
                if -50 < (en.y - blt.y) < 50 and -50 < (en.x - blt.x) < 50:
                    self.kill += 1
                    self.enemies.remove(en)
                    if blt in self.bullets:
                        self.bullets.remove(blt)

                # Controlla se il proiettile esce dalla mappa
                if blt.y <= -1:
                    if blt in self.bullets:
                        self.bullets.remove(blt)

            # Se hai perso
            if self.lost:
                self.bullets.remove(blt)
                self.player.cool_down_counter = 0

        # Genera un cuore ogni 15 secondi
        if self.heart_cool_down <= 0:
            heart = bonus.Heart(random.randint(70, settings.WIDTH - 100), random.randint(-250, -100))
            self.hearts.append(heart)
            self.heart_cool_down = settings.FPS * settings.HEART_COOL_DOWN

        # Sposta il cuore
        for heart in self.hearts:

            # Controlla se il cuore esce dalla mappa
            if heart.y >= settings.HEIGHT + 50:
                self.hearts.remove(heart)

            # Controlla se il cuore collide con il player
            if -50 < (heart.y - self.player.y) < 50 and -50 < (heart.x - self.player.x) < 50:
                self.lives += 1
                self.hearts.remove(heart)

            # if you lose
            if self.lost:
                # remove all hearts
                self.hearts.remove(heart)
                self.heart_cool_down = 0

    def play(self):
        """Metodo play, implementa la struttura base del gioco"""
        while self.run:
            self.clock.tick(settings.FPS)
            self.update_window()
            self.is_dead()
            self.has_lost()
            self.are_enemies_death()
            self.quit_application()
            self.pressed_key()
            self.move()
            self.collision_detector()
