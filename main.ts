radio.onReceivedNumber(function (receivedNumber) {
    if (true) {
        basic.showLeds(`
            # # # # #
            # . . . .
            # # # . .
            # . . . .
            # . . . .
            `)
    }
})
// Make it so it does the 3,2,1 countdown tune
input.onButtonPressed(Button.A, function () {
    basic.pause(1000)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showString("Go!")
})
let Bpressed = 0
let km = 0
let steps = 0
radio.setGroup(234)
basic.showString("Press a to start")
// Ver 2
// 
// Ver 2
// On average, it takes roughly 1,200 to 1,500 steps to walk one kilometer while it can take between 900 and 1250 steps to run a kilometer. If your goal is to walk 10,000 steps a day, it will take a little over 8 kilometers of travel to reach that goal. To successfully communicate through Python, I will be using abstraction and will define a kilometer as 1250 steps, as a microbit cannot distinguish running from walking.
basic.forever(function () {
    if (input.acceleration(Dimension.Strength) > 1500) {
        steps += 1
        basic.showNumber(steps)
        radio.sendNumber(steps)
        if (steps == 1250) {
            km += 1
            basic.showNumber(km)
            radio.sendNumber(km)
        }
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.pause(1000)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        Bpressed = 0
        while (Bpressed == 0) {
        	
        }
        basic.showString("Go!")
        if (input.buttonIsPressed(Button.B)) {
            Bpressed = 1
            control.reset()
        }
    }
})
