import pygame
from models.WallFactory import WallFactory
import random

class Map:
    """Grid-based map system"""

    def __init__(self, cols=20, rows=15, tile_size=32):
        self.cols = cols
        self.rows = rows
        self.tile_size = tile_size
        self.grid = []

        for row in range(self.rows):
            for col in range(self.cols):
                x = col * tile_size
                y = row * tile_size

                # --- Kenarlar: unbreakable duvarlar ---
                if row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1:
                    wall = WallFactory.create_wall("unbreakable", x, y)
                    self.grid.append(wall)

                # --- Her iki satır ve sütunda hard wall (mor) ---
                elif row % 2 == 0 and col % 2 == 0:
                    wall = WallFactory.create_wall("hard", x, y)
                    self.grid.append(wall)

                # --- Boş alanlar: bazen breakable duvar (kahverengi), bazen boş ---
                else:
                    # Oyuncunun doğacağı bölgeyi boş bırak (sol üst 2x2 alan)
                    if (row < 2 and col < 2):
                        continue
                    # %30 olasılıkla kırılabilir duvar koy
                    elif random.random() < 0.3:
                        wall = WallFactory.create_wall("breakable", x, y)
                        self.grid.append(wall)
                    # Aksi halde boş (hiçbir şey ekleme)

    def draw(self, screen):
        for wall in self.grid:
            wall.draw(screen)



    def get_random_empty_position(self):
        """Haritadaki boş alanlardan rastgele bir pozisyon döndürür"""
        occupied = [(w.x, w.y) for w in self.grid]
        all_positions = []

        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_size
                y = row * self.tile_size
                all_positions.append((x, y))

        # Duvar olmayan pozisyonları bul
        empty_positions = [pos for pos in all_positions if pos not in occupied]


        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_size
                y = row * self.tile_size
                all_positions.append((x, y))

        # Duvar olmayan pozisyonları bul
        empty_positions = [pos for pos in all_positions if pos not in occupied]

        # Rastgele bir boş pozisyon seç
        if empty_positions:
            return random.choice(empty_positions)
        else:
            return (64, 64)  # fallback (asla olmamalı)