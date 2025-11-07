import pygame

class Player:
    def __init__(self, x, y, speed):
        """
        Oyuncunun başlangıç konumu ve hızı tanımlanır.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 32
        self.color = (200, 50, 50)  # kırmızı

    def move(self, keys):
        """
        Klavyedeki yön tuşlarına göre hareket ettirir.
        """
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, screen):
        """
        Oyuncuyu ekrana çizer (kırmızı kare)
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))