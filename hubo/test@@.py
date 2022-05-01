from cs1robots import *#휴보관련 함수를 모두 불러온다
load_world("worlds/amazing1.wld")#rain2라는 맵을 불러온다
hubo = Robot(beepers=10, avenue=2, street=6)#휴보가 2,6에서 20개의 비퍼를 가지고 소환돤다
hubo.set_pause(0.01)#휴보의 모든 행동이 0.01초의 간격을 두고 행동을 한다
hubo.set_trace("blue")
def turn_right():#휴보가 과정적으로는 3번 왼쪽으로 이동하지만 결과적으로는 오른쪽으로 이동하게 함수를 쓴다.
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()#왼쪽벽을 타고 가겠금한다
def go():
    if hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            while not hubo.on_beeper():
                hubo.pick_beeper()
def left_c():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
def right_c():
    turn_right()
    hubo.move()
    turn_right()
go()
left_c()
right_c()
go()
left_c()
right_c()

