import tdl
from arroguella.objects import player as p, game_object as obj

# Constants
SCREEN_WIDTH = 85
SCREEN_HEIGHT = 55
FONT='arroguella/fonts/consolas_unicode_12x12.png'
LIMIT_FPS = 20
REALTIME = True
DEFAULT_BG = (30, 30, 40)
DEFAULT_FG = (220, 220, 220)

# Game engine variables
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
    objects['player'].handle_key(key=user_input.key)


# blit the contents of the src console to the dst console, to display them.
# source rectangle has its top-left corner at coordinates (0, 0)
# and is the same size as the screen;
# the destination coordinates are (0, 0) as well.
def blit(src, dst):
    dst.blit(src, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)


def draw_objects():
    for k, v in objects.items():
        v.draw(con, bg=DEFAULT_BG)
    blit(con, root)
    tdl.flush()
    for k, v in objects.items():
        v.clear(con, bg=DEFAULT_BG)


def initialize():
    global root, con, objects
    # Set up console
    tdl.set_font(FONT, greyscale=False, altLayout=False)
    tdl.setFPS(LIMIT_FPS)
    # Root Console
    root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Arroguella", fullscreen=False)
    # Game Console
    con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    con.clear(fg=DEFAULT_FG, bg=DEFAULT_BG)
    # Set up initial objects
    npc = obj.GameObject(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2, '@', (255,90,0))
    player = p.Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    objects['player'] = player
    objects['npc'] = npc



def run_main_loop():
    while not tdl.event.is_window_closed():
        draw_objects()
        exit_game = handle_keys()
        if exit_game:
            break


def run():
    print ('Starting Arroguella ... ')
    initialize()
    run_main_loop()
    print (' ... exited Arroguella.')
