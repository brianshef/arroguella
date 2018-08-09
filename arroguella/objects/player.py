from . import game_object as obj


class Player(obj.GameObject):
    """Player class represents the player character."""
    # Constructor
    def __init__(self, x=0, y=0, char='@', color=(255, 255, 255), name='Player'):
        super().__init__(x, y, char, color)
        # Basic Info
        self.name = name
        self.level = 1
        self.xp = 0


    def draw(self, console, visible_tiles, bg=None):
        console.draw_char(self.x, self.y, self.char, self.color, bg=bg)


    # Movement according to user input
    # Return whether or not the player moved based on the key input
    def handle_key(self, key, tile_map):
        if key == 'UP':
            self.move(0, -1, tile_map)
        elif key == 'DOWN':
            self.move(0, 1, tile_map)
        elif key == 'LEFT':
            self.move(-1, 0, tile_map)
        elif key == 'RIGHT':
            self.move(1, 0, tile_map)
        else:
            return False
        return True
