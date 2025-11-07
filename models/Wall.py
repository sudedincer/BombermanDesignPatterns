import pygame

class Wall:
    """Abstract base wall class"""
    def __init__(self, x, y, color, breakable=False, hitPoints=1):
        self.x = x
        self.y = y
        self.color = color
        self.size = 32
        self.breakable = breakable
        self.hitPoints = hitPoints  # hard walls require multiple hits

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def destroy(self):
        """Reduce hit points or mark as destroyed"""
        if self.breakable:
            self.hitPoints -= 1
            if self.hitPoints <= 0:
                return True  # destroyed
        return False


# --- Alt sınıflar ---
class BreakableWall(Wall):
    def __init__(self, x, y):
        super().__init__(x, y, color=(190, 120, 60), breakable=True, hitPoints=1)


class UnbreakableWall(Wall):
    def __init__(self, x, y):
        super().__init__(x, y, color=(80, 80, 80), breakable=False, hitPoints=999)


class HardWall(Wall):
    def __init__(self, x, y):
        super().__init__(x, y, color=(120, 50, 150), breakable=True, hitPoints=3)