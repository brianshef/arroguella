# Constants
SYMBOL = '@'
FG = (255, 255, 255)

class Player:
    """Player class represents the player character."""
    # Constructor
    def __init__(self, name='Frodo Baggins', start_x=1, start_y=1):
        # Basic Info
        self.name = name
        self.level = 1
        self.xp = 0

        # System Info
        self.x = start_x
        self.y = start_y
        self.appearance = SYMBOL
        self.color = FG


    # Movement
    def handle_key(self, key=None):
        if key == 'UP':
            self.move(delta_y=-1)
        elif key == 'DOWN':
            self.move(delta_y=1)
        elif key == 'LEFT':
            self.move(delta_x=-1)
        elif key == 'RIGHT':
            self.move(delta_x=1)


    def move(self, delta_x=0, delta_y=0):
        self.x += delta_x
        self.y += delta_y
