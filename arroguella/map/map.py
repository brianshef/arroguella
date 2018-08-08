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
        self.tiles = [[ tile.Tile(False)
            for y in range(self.height) ]
                for x in range(self.width) ]
        # Two "columns"
        self.tiles[30][22].block()
        self.tiles[50][22].block()


    def render(self, console):
        for y in range(self.height):
            for x in range(self.width):
                wall = self.tiles[x][y].block_sight
                bg = colors.WALLS['dark_wall'] if wall else colors.TERRAIN['dark_ground']
                console.draw_char(x, y, None, fg=None, bg=bg)
