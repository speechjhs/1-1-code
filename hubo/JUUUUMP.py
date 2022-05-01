from cs1robots import *
load_world("worlds/hurdles4.wld")
hubo= Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)
def turn_right():
    for i in range(3):
        hubo.turn_left()
def jump_one_hurdle():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
def jump_mul_hurdle():
    hubo.turn_left()
    while not hubo.right_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

def move_jump_or_finish():
    if hubo.on_beeper():
        pass
    elif hubo.front_is_clear():
        hubo.move()
    else:
        jump_mul_hurdle()
while not hubo.on_beeper():
    move_jump_or_finish()