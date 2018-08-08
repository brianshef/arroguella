from . import tile
from . import colors


class Map:
    # The representation of the playable game space in which tiles and objects exist
    def __init__(self, width=85, height=50):
        self.width = width
        self.height = height
        self.tiles = {}
        self.make_map()


    def make_map(self):
        # Fill map with unblocked tiles
        self.tiles = [[ tile.Tile(blocked=True)
            for y in range(self.height) ]
                for x in range(self.width) ]
        # Make some rooms
        self.create_room(room=Rect(20, 15, 10, 15))
        self.create_room(room=Rect(50, 15, 10, 15))
        self.create_h_tunnel(25, 55, 23)


    def set_tile_blocked(self, x, y, blocked=True):
        self.tiles[x][y].block(blocked)


    def render(self, console):
        for y in range(self.height):
            for x in range(self.width):
                wall = self.tiles[x][y].block_sight
                bg = colors.WALLS['dark_wall_bg'] if wall else colors.TERRAIN['dark_ground_bg']
                char = '#' if wall else '.'
                fg = colors.WALLS['dark_wall_fg'] if wall else colors.TERRAIN['dark_ground_fg']
                console.draw_char(x, y, char, fg=fg, bg=bg)


    # Creates a rectangualr room of non-blocked tiles
    def create_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.set_tile_blocked(x, y, blocked=False)


    # Create a horizontal tunnel of non-blocked tiles
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.set_tile_blocked(x, y, blocked=False)


    # Create a vertical tunnel of non-blocked tiles
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.set_tile_blocked(x, y, blocked=False)


class Rect:
    # A rectangle on the map. Used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
