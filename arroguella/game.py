import tdl
from arroguella.player import player as p

# Constants
SCREEN_WIDTH = 85
SCREEN_HEIGHT = 55
FONT='arroguella/fonts/consolas_unicode_12x12.png'
LIMIT_FPS = 20
REALTIME = True
DEFAULT_BG = (30, 30, 40)
DEFAULT_FG = (220, 220, 220)

# Game engine variables
player = None
console = None


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
    player.handle_key(key=user_input.key)


def update_char():
    console.draw_char(player.x, player.y, player.appearance, bg=DEFAULT_BG, fg=player.color)
    tdl.flush()
    console.draw_char(player.x, player.y, ' ', bg=DEFAULT_BG)


def initialize():
    global console, player
    # Set up console
    tdl.set_font(FONT, greyscale=False, altLayout=False)
    tdl.setFPS(LIMIT_FPS)
    console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Arroguella", fullscreen=False)
    console.clear(fg=DEFAULT_FG, bg=DEFAULT_BG)
    # Set up player
    player = p.Player(start_x=(SCREEN_WIDTH//2), start_y=(SCREEN_HEIGHT//2))


def run_main_loop():
    while not tdl.event.is_window_closed():
        update_char()
        exit_game = handle_keys()
        if exit_game:
            break


def run():
    print ('Starting Arroguella ... ')
    initialize()
    run_main_loop()
    print (' ... exited Arroguella.')
