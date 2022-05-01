k = 0
from cs1robots import *
load_world("worlds/trash2.wld")
hubo = Robot(beepers=1, avenue=1, street=1)
hubo.set_pause(0.01)
hubo.set_trace("blue")

def turn_back():
    hubo.turn_left()
    hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def follow_right_wall():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
        turn_back()
        hubo.drop_beeper()
        hubo.move()
        hubo.turn_left()
    elif hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
    else:
        hubo.turn_left()
hubo.move()
if hubo.on_beeper():
    hubo.pick_beeper()
hubo.move()
if hubo.on_beeper():
    hubo.pick_beeper()

while hubo.carries_beepers():
    follow_right_wall()



