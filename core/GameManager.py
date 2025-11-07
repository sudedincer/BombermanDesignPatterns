import pygame
from models.Player import Player

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
        self.screen = pygame.display.set_mode((640, 480))  # pencere boyutu
        pygame.display.set_caption("Bomberman – Week 1")   # pencere başlığı
        self.clock = pygame.time.Clock()                   # FPS kontrolü
        self.running = True

        # Oyuncu nesnesi oluştur
        self.player = Player(300, 220, 5)

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
            self.player.move(keys)

            # Ekranı temizle
            self.screen.fill((30, 30, 30))  # koyu gri arka plan

            # Oyuncuyu çiz
            self.player.draw(self.screen)

            # Ekranı güncelle
            pygame.display.flip()

            # FPS sınırı (60 kare/sn)
            self.clock.tick(60)

        pygame.quit()