function button_home_pressed () {
    if (input.logoIsPressed()) {
        home_pressed = 1
        timer = 30
        basic.showIcon(IconNames.SmallSquare)
        basic.pause(1000)
        basic.showIcon(IconNames.Square)
        basic.pause(1000)
        basic.showIcon(IconNames.SmallDiamond)
        basic.pause(1000)
        basic.showIcon(IconNames.Diamond)
        basic.pause(1000)
        basic.showIcon(IconNames.SmallSquare)
        basic.pause(1000)
        basic.showIcon(IconNames.Square)
        basic.clearScreen()
        if_home_pressed__HIGH()
    }
    return 0
}
function if_home_pressed__HIGH () {
    if (home_pressed == 1) {
        if (time0 == 0) {
            basic.showString("" + timer)
            basic.pause(1000)
            timer += -1
        } else {
            basic.clearScreen()
            music.playMelody("C D E F E D C D ", 120)
            time0 = 0
            home_pressed = 0
        }
        if (timer < 0) {
            time0 = 1
        }
    } else {
        basic.clearScreen()
    }
}
let timer = 0
let time0 = 0
let home_pressed = 0
home_pressed = 0
time0 = 0
basic.forever(function () {
    if (home_pressed != 1) {
        button_home_pressed()
    } else {
        if_home_pressed__HIGH()
    }
})
