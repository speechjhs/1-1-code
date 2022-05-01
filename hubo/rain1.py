from cs1robots import *
load_world("worlds/rain1.wld")
hubo = Robot(beepers=1, avenue=2, street=6)
hubo.set_pause(1)
hubo.set_trace("blue")

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
"""
def follow_right_wall():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
while not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
while not hubo.on_beeper():v 
    follow_right_wall()
"""
hubo.move()
def follow_left_wall():
    if hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
        if hubo.left_is_clear() and hubo.right_is_clear():
            hubo.turn_left()
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()
            hubo.move()
        else:
            pass


    elif hubo.front_is_clear():
        hubo.move()
    else:
        turn_back()
def turn_back():
    hubo.turn_left()
    hubo.turn_left()


while not hubo.on_beeper():
    follow_left_wall()