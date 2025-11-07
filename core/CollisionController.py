import pygame

class CollisionController:
    """Oyuncu ile duvarlar arasındaki çarpışmayı kontrol eder"""

    @staticmethod
    def check_collision(player, walls):
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)

        for wall in walls:
            wall_rect = pygame.Rect(wall.x, wall.y, wall.size, wall.size)
            #çarğışma sert olmaması için tolerns 
            if player_rect.colliderect(wall_rect.inflate(-4, -4)): 
                return True  # çarpışma var
        return False