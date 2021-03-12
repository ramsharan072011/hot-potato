def button_home_pressed():
    global home_pressed, timer
    if input.logo_is_pressed():
        home_pressed = 1
        timer = 30
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.pause(1000)
        basic.show_icon(IconNames.SQUARE)
        basic.pause(1000)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.pause(1000)
        basic.show_icon(IconNames.DIAMOND)
        basic.pause(1000)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.pause(1000)
        basic.show_icon(IconNames.SQUARE)
        basic.clear_screen()
        if_home_pressed__HIGH()
    return 0
def if_home_pressed__HIGH():
    global timer, time0, home_pressed
    if home_pressed == 1:
        if time0 == 0:
            basic.show_string("" + str(timer))
            basic.pause(1000)
            timer += -1
        else:
            basic.clear_screen()
            music.play_melody("C D E F E D C D ", 120)
            time0 = 0
            home_pressed = 0
        if timer < 0:
            time0 = 1
    else:
        basic.clear_screen()
timer = 0
time0 = 0
home_pressed = 0
home_pressed = 0
time0 = 0

def on_forever():
    if home_pressed != 1:
        button_home_pressed()
    else:
        if_home_pressed__HIGH()
basic.forever(on_forever)
