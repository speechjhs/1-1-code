from cs1robots import *#처음에 hubo관련 모듈을 가지고 온다
load_world("worlds/hurdles3.wld")#hurdles3라는 맵을 불러온다
hubo= Robot()#휴보를 소환해 준다
hubo.set_trace("blue")#휴보의 움직임의 흔적을 파란색으로 칠한다.
hubo.set_pause(0.01)#0.01초의 간격을 두고 휴보가 행동을 한다
def turn_right():#오른쪽으로도는 함수를 만든다
    for i in range(3):
        hubo.turn_left()
def jump_one_hurdle():#높이가 1인 허들을 넘는 함수를 만든다
    hubo.turn_left()#왼쪽으로 돈다
    hubo.move()#앞으로 간다
    turn_right()#오른쪽으로 돈다
    hubo.move()#앞으로 간다
    turn_right()#오른쪽으로 돈다
    hubo.move()#앞으로 간다
    hubo.turn_left()#왼쪽으로 돈다
def move_jump_or_finish():
    if hubo.on_beeper():#결승선에 도착했을 떄 코드를 종료한다.
        pass
    elif hubo.front_is_clear():#허들간의 간격이 있을 것을 대비하여 간격이 없어질 때까지 앞으로 이동시킨다
        hubo.move()
    else:#허들을 만났을 때 작동된다.
        pass
while not hubo.on_beeper():#결승선에 도착할 때까지 점프를 하게 한다.
    move_jump_or_finish()