from models.Wall import BreakableWall, UnbreakableWall, HardWall

class WallFactory:
    """Factory class to create different types of walls"""

    @staticmethod
    def create_wall(wall_type, x, y):
        if wall_type == "breakable":
            return BreakableWall(x, y)
        elif wall_type == "unbreakable":
            return UnbreakableWall(x, y)
        elif wall_type == "hard":
            return HardWall(x, y)
        else:
            raise ValueError(f"Unknown wall type: {wall_type}")