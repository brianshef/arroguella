import tdl
from arroguella.objects import player as p, game_object as obj
from arroguella.map import map as m


# Constants
SCREEN_WIDTH = 85
SCREEN_HEIGHT = 55
FONT='arroguella/fonts/consolas_unicode_12x12.png'
LIMIT_FPS = 20
REALTIME = True
FOV_ALGO = 'BASIC'
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

# Game engine variables
map = None
objects = {}
root = None
con = None

def handle_realtime_keys():
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
           return event
    return None


def handle_turnbased_keys():
    return tdl.event.key_wait()


def handle_keys():
    user_input = handle_realtime_keys() if REALTIME else handle_turnbased_keys()
    if not user_input:
        return
    if user_input.key == 'ENTER' and user_input.alt:
        tdl.set_fullscreen(not tdl.get_fullscreen())
    elif user_input.key == 'ESCAPE':
        return True  # exit game
    moved = objects['player'].handle_key(key=user_input.key, tile_map=map.tiles)


# Use the map object to calculate whether or not a tile at the coordinates is visible
def is_visible_tile(x, y):
    map.is_visible_tile(x, y)


# blit the contents of the src console to the dst console, to display them.
# source rectangle has its top-left corner at coordinates (0, 0)
# and is the same size as the screen;
# the destination coordinates are (0, 0) as well.
def blit(src, dst):
    dst.blit(src, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)


def render_all():
    visible_tiles = tdl.map.quickFOV(
        objects['player'].x, objects['player'].y,
        is_visible_tile,
        fov=FOV_ALGO,
        radius=TORCH_RADIUS,
        lightWalls=FOV_LIGHT_WALLS
    )
    map.render(con, visible_tiles)
    for k, v in objects.items():
        v.draw(con, visible_tiles)
    blit(con, root)
    tdl.flush()
    for k, v in objects.items():
        v.clear(con)


def initialize():
    global root, con, objects, map
    # Set up console
    tdl.set_font(FONT, greyscale=False, altLayout=False)
    tdl.setFPS(LIMIT_FPS)
    # Root Console
    root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Arroguella", fullscreen=False)
    # Game Console
    con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    con.clear(fg=(0,0,0), bg=(0,0,0))
    # Set up map
    map = m.Map(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    # # Optional: Print room labels
    # for k, r in map.rooms.items():
    #     objects[k] = obj.GameObject(*r.center(), k, color=(20, 20, 20))
    # Set up initial objects
    player = p.Player(*map.player_start)
    objects['player'] = player


def run_main_loop():
    while not tdl.event.is_window_closed():
        render_all()
        exit_game = handle_keys()
        if exit_game:
            break


def run():
    print ('Starting Arroguella ... ')
    initialize()
    run_main_loop()
    print (' ... exited Arroguella.')
