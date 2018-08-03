import tdl

# Constants
SCREEN_WIDTH = 85
SCREEN_HEIGHT = 55
FONT='arroguella/fonts/consolas_unicode_12x12.png'
LIMIT_FPS = 20
REALTIME = True

# Game engine variables
console = None
playerchar = '@'
player_fg = (255, 255, 255)
emptychar = ' '
playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2


def handle_realtime_keys():
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
           return event
    return None


def handle_turnbased_keys():
    return tdl.event.key_wait()


def handle_keys():
    global playerx, playery
    user_input = handle_realtime_keys() if REALTIME else handle_turnbased_keys()
    if not user_input:
        return
    if user_input.key == 'ENTER' and user_input.alt:
        tdl.set_fullscreen(not tdl.get_fullscreen())
    elif user_input.key == 'ESCAPE':
        return True  # exit game
    if user_input.key == 'UP':
        playery -= 1
    elif user_input.key == 'DOWN':
        playery += 1
    elif user_input.key == 'LEFT':
        playerx -= 1
    elif user_input.key == 'RIGHT':
        playerx += 1


def draw_char(display=True):
    if display:
        console.draw_char(playerx, playery, playerchar, bg=None, fg=player_fg)
    else:
        console.draw_char(playerx, playery, emptychar, bg=None)


def update_char():
    draw_char(display=True)
    tdl.flush()
    draw_char(display=False)


def initialize():
    global console
    tdl.set_font(FONT, greyscale=False, altLayout=False)
    console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Arroguella", fullscreen=False)
    tdl.setFPS(LIMIT_FPS)


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
