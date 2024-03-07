def on_received_number(receivedNumber):
    if True:
        basic.show_leds("""
            # # # # #
            # . . . .
            # # # . .
            # . . . .
            # . . . .
            """)
radio.on_received_number(on_received_number)

# Make it so it does the 3,2,1 countdown tune

def on_button_pressed_a():
    basic.pause(1000)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("Go!")
input.on_button_pressed(Button.A, on_button_pressed_a)

Bpressed = 0
km = 0
steps = 0
radio.set_group(234)
basic.show_string("Press a to start")
# Ver 2
# 
# Ver 2
# On average, it takes roughly 1,200 to 1,500 steps to walk one kilometer while it can take between 900 and 1250 steps to run a kilometer. If your goal is to walk 10,000 steps a day, it will take a little over 8 kilometers of travel to reach that goal. To successfully communicate through Python, I will be using abstraction and will define a kilometer as 1250 steps, as a microbit cannot distinguish running from walking.

def on_forever():
    global steps, km
    if input.acceleration(Dimension.STRENGTH) > 1500:
        steps += 1
        basic.show_number(steps)
        radio.send_number(steps)
        if steps == 1250:
            km += 1
            basic.show_number(km)
            radio.send_number(km)
basic.forever(on_forever)

def on_forever2():
    global Bpressed
    if input.button_is_pressed(Button.A):
        basic.pause(1000)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        Bpressed = 0
        while Bpressed == 0:
            pass
        basic.show_string("Go!")
        if input.button_is_pressed(Button.B):
            Bpressed = 1
            control.reset()
basic.forever(on_forever2)
