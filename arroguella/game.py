import tdl

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FONT='arroguella/fonts/consolas_unicode_12x12.png'
LIMIT_FPS = 20


def initialize():
    tdl.set_font(FONT, greyscale=False, altLayout=False)
    console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Arroguella", fullscreen=False)
    tdl.setFPS(LIMIT_FPS)
    return console


def run_main_loop(console):
    while not tdl.event.is_window_closed():
        console.draw_char(1, 1, '@', bg=None, fg=(255,255,255))
        tdl.flush()


def run():
    print ('Starting Arroguella ... ')
    console = initialize()
    run_main_loop(console)
    print (' ... exited Arroguella.')
