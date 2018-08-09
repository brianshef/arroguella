from . import game_object as obj

class Monster(obj.GameObject):
    # Constructor
    def __init__(self, x=0, y=0, char='X', color=(205, 55, 0), name='monster'):
        super().__init__(x, y, char, color, name, blocks=True)
        # Basic Info
        self.spotted = False


    def draw(self, console, visible_tiles, bg=None):
        # draw the character that represents this object at its position
        if (self.x, self.y) in visible_tiles or self.spotted:
            console.draw_char(self.x, self.y, self.char, self.color, bg=bg)
            if not self.spotted:
                if self.name: print('You see a', self.name, '!')
                self.spotted = True
        elif self.spotted:
            console.draw_char(self.x, self.y, self.char, self.color, bg=bg)
