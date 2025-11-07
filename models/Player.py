import pygame

class Player:
    def __init__(self, x, y, speed):
        """
        Oyuncunun başlangıç konumu ve hızı tanımlanır.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 24  # oyuncu boyutu
        self.color = (200, 50, 50)  # kırmızı

    def move(self, keys, walls=None):
        """
        Klavyedeki yön tuşlarına göre hareket ettirir.
        """
        old_x, old_y = self.x, self.y  # eski konum yedekle

        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    # Eğer duvar listesi verilmişse çarpışmayı kontrol et
        if walls:
            from core.CollisionController import CollisionController
            if CollisionController.check_collision(self, walls):
             # Çarpışma varsa konumu geri al
                self.x, self.y = old_x, old_y

    def draw(self, screen):
        """
        Oyuncuyu ekrana çizer (kırmızı kare)
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))