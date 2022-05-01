from cs1robots import *#휴보의 모든 함수를 불러온다
load_world("worlds/rain1.wld")#rain1이라는 맵을 불러온다
hubo = Robot(beepers=6, avenue=2, street=6)#(2,6)에서 처음 출발하고 비퍼를 6개를 처음에 가지고 있다
hubo.set_pause(0.01)#휴보의 모든 행동을 0.01초간을 간격을 두고 행동을 한다
hubo.set_trace("blue")#휴보의 모든 행동의 자취를 파란색으로 칠한다
hubo.move()
hubo.drop_beeper()
hubo.turn_left()
hubo.move()
#위 코드들은 초반 휴보의 위치 설정과 행동의 기준을 세우기 위해 만들었다
def turn_right():#휴보가 결과적으로는 오른쪽으로 돌도록 왼쪽으로 3번 돌게하는 함수를 선언한다
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def follow_left_wall():#휴보다 왼쪽 벽을 따라가도록 코드를 짰다
    if hubo.front_is_clear():
        hubo.move()
    else:
        turn_right()

while not hubo.on_beeper():


    if hubo.left_is_clear():
        hubo.drop_beeper()
        hubo.move()
    #창문을 지나갈 때 비퍼를 내려 놓는다
    #그렇다가 마지막 처음위치에서 while문을 종료한다.
    follow_left_wall()