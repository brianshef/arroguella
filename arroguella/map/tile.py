class Tile:
    # A tile of the map and its properties
    def __init__(self, blocked, block_sight=None, color=(255, 0, 255)):
        self.explored = False
        self.blocked = blocked
        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight


    def block(self, blocked=True):
        self.blocked = blocked
        self.block_sight = blocked
