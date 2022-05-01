from cs1robots import *#휴보 관련 모든 함수를 불러온다
load_world("worlds/maze1.wld")#maze1라는 맵을 불러온다
hubo = Robot(beepers=1, avenue=1, street=1)#휴보가 비퍼하나에, 1,1에서 소환되게 한다
hubo.set_pause(0.01)#휴보의 모든 행동에 0.01초의 간격을 두고하게한다
hubo.set_trace("blue")#휴보의 모든 행동의 자취를 파란색으로 남긴다

def turn_right():#휴보가 오론쪽으로 도는 함수를 만든다
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()#왼쪽으로 총 3번 돌아 결과적으로 오른쪽으로 돌겠금 했다

def follow_left_wall():#휴보가 왼쪽벽을 따라 움직이게 하는 함수를 만든다
    if hubo.left_is_clear():#왼쪽에 벽이 없다면 왼쪽으로 돌고 앞으로 이동한다
        hubo.turn_left()#왼쪽으로 돈다
        hubo.move()#앞으로 간다
    elif hubo.front_is_clear():#왼쪽에 벽이 있고 앞에 벽이 없는 상황에서 앞으로 휴보가 앞으로 이동하게 한다
        hubo.move()#앞으로 간다
    else:
        turn_back()#휴보가 골목을 마주했을 때 빙빙도는 상황을 방지하기 위해 썼다.
def turn_back():#turn_back이라는 함수를 만들었다.
    hubo.turn_left()#왼쪽으로 돈다
    hubo.turn_left()#왼쪽으로 돈다
while not hubo.front_is_clear():#초반에 휴보의 방향을 잡기 위해 만들었다
    hubo.turn_left()#왼쪽으로 돈다
hubo.move()
while not hubo.on_beeper():#휴보가 결승선에 도착하기 전까지 실행하게 한다.\
    follow_left_wall()#follow_left_wall함수 실행()함수 콜