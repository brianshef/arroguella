from . import game_object as obj


class Player(obj.GameObject):
    """Player class represents the player character."""
    # Constructor
    def __init__(self, x, y, char='@', color=(255, 255, 255), name='Frodo Baggins'):
        super().__init__(x, y, char, color)
        # Basic Info
        self.name = name
        self.level = 1
        self.xp = 0


    # Movement
    def handle_key(self, key=None):
        if key == 'UP':
            self.move(0, -1)
        elif key == 'DOWN':
            self.move(0, 1)
        elif key == 'LEFT':
            self.move(-1, 0)
        elif key == 'RIGHT':
            self.move(1, 0)
