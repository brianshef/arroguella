class GameObject:
    # this is a generic object: the player, a monster, an item, the stairs...
    # it's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color


    def move(self, dx, dy, tile_map):
        # move by the given amount, IFF the tile is not blocked
        tile = tile_map[self.x + dx][self.y + dy]
        if not tile.blocked:
            self.x += dx
            self.y += dy


    def draw(self, console, visible_tiles, bg=None):
        # draw the character that represents this object at its position
        if visible_tiles is None or (self.x, self.y) in visible_tiles:
            console.draw_char(self.x, self.y, self.char, self.color, bg=bg)


    def clear(self, console, bg=None):
        # erase the character that represents this object
        console.draw_char(self.x, self.y, ' ', self.color, bg=bg)
