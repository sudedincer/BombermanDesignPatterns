import pygame
from models.Player import Player
from models.Map import Map

class GameManager:
    __instance = None  # Singleton için özel değişken

    @staticmethod
    def get_instance():
        """
        GameManager sınıfının tek örneğini döndürür.
        Daha önce oluşturulmadıysa oluşturur.
        """
        if GameManager.__instance is None:
            GameManager()
        return GameManager.__instance

    def __init__(self):
        """
        Sınıf oluşturulduğunda çalışır.
        Eğer zaten bir örnek varsa, tekrar oluşturulmasını engeller.
        """
        if GameManager.__instance is not None:
            raise Exception("GameManager zaten oluşturuldu!")
        else:
            GameManager.__instance = self

        # --- Oyun ekranını ve bileşenleri başlat ---
        pygame.init()
        self.screen = pygame.display.set_mode((520, 450))  # pencere boyutu
        pygame.display.set_caption("Bomberman – Week 1")   # pencere başlığı
        self.clock = pygame.time.Clock()                   # FPS kontrolü
        self.running = True

        # Harita nesnesi oluştur
        self.map = Map(15, 13)
        # Oyuncu nesnesi oluştur, rastgele boş bir alanda başlat
        x, y = self.map.get_random_empty_position()
        self.player = Player(x, y, 4)

    def run(self):
        """
        Oyun döngüsünü (game loop) çalıştırır.
        Her frame'de:
        - eventleri okur
        - oyuncuyu hareket ettirir
        - ekranı çizer
        """
        while self.running:
            # Kullanıcıdan gelen olayları al
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Klavye tuşlarını al
            keys = pygame.key.get_pressed()
            self.player.move(keys, self.map.grid)

            # Ekranı temizle
            self.screen.fill((30, 30, 30))  # koyu gri arka plan

            # Oyuncuyu ve haritayı çiz
            self.screen.fill((30, 30, 30))
            self.map.draw(self.screen)
            self.player.draw(self.screen)

            # Ekranı güncelle
            pygame.display.flip()

            # FPS sınırı (60 kare/sn)
            self.clock.tick(60)

        pygame.quit()