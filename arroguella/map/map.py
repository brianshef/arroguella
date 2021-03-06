from . import tile
from . import colors
from .geometry import rect
from random import randint


ROOM_MAX_SIZE = 26
ROOM_MIN_SIZE = 5
MAX_ROOMS = 26


class Map:
    # The representation of the playable game space in which tiles and objects exist
    def __init__(self, width=85, height=50):
        self.width = width
        self.height = height
        self.rooms = {}
        self.tiles = {}
        self.player_start = (width//2, height//2)
        self.make_map()


    def make_map(self):
        # Fill map with unblocked tiles
        self.tiles = [[ tile.Tile(blocked=True)
            for y in range(self.height) ]
                for x in range(self.width) ]
        # Make some rooms
        for r in range(MAX_ROOMS):
            w = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            x = randint(0, self.width-w-1)
            y = randint(0, self.height-h-1)
            new_room = rect.Rect(x, y, w, h)
            failed = False
            for other_room in list(self.rooms.values()):
                if new_room.intersect(other_room):
                    failed = True
                    break
            if not failed:
                self.create_room(room=new_room)
                (new_x, new_y) = new_room.center()
                if len(self.rooms) == 0:
                    # this is the first room, where the player starts at
                    self.player_start = (new_x, new_y)
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel
                    # center coordinates of previous room
                    (prev_x, prev_y) = list(self.rooms.values())[len(self.rooms)-1].center()
                    if randint(0, 1):
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                # finally, append the new room to the list
                self.rooms[chr(65+len(self.rooms))] = new_room
        # # Debug:
        # for k, v in self.rooms.items(): print(k, v.center())



    def set_tile_blocked(self, x, y, blocked=True):
        self.tiles[x][y].block(blocked)


    def is_visible_tile(self, x, y):
        if x >= self.width or x < 0:
            return False
        elif y >= self.height or y < 0:
            return False
        elif self.tiles[x][y].blocked or self.tiles[x][y].block_sight:
            return True
        else:
            return True


    def render(self, console, visible_tiles):
        for y in range(self.height):
            for x in range(self.width):
                visible = (x, y) in visible_tiles
                wall = self.tiles[x][y].block_sight
                char = '#' if wall else '.'
                if not visible:
                    # It's out of the player's FOV / it's dark
                    # If it's not visible right now, the player can only see it if it's explored
                    if self.tiles[x][y].explored:
                        if wall:
                            console.draw_char(x, y, char, fg=colors.WALLS['dark_wall_fg'], bg=colors.WALLS['dark_wall_bg'])
                        else:
                            console.draw_char(x, y, char, fg=colors.TERRAIN['dark_ground_fg'], bg=colors.TERRAIN['dark_ground_bg'])
                else:
                    # It's visible in FOV / it's light
                    if wall:
                        console.draw_char(x, y, char, fg=colors.WALLS['light_wall_fg'], bg=colors.WALLS['light_wall_bg'])
                    else:
                        console.draw_char(x, y, char, fg=colors.TERRAIN['light_ground_fg'], bg=colors.TERRAIN['light_ground_bg'])
                    # Since it's visible, explore it:
                    self.tiles[x][y].explored = True


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
