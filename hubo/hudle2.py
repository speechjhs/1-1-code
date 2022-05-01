from cs1robots import *#휴보 관련 함수를 모두 불러온다
load_world("worlds/hurdles4.wld")#hurdles4라는 맵을 불러온다
hubo = Robot(beepers=1, avenue=1, street=1)#휴보가 (1,1)에서 비퍼를 하나 가지고 있는 상태에서 시작하게 한다
hubo.set_pause(0.01)#모든 휴보의 행동에서 0.01초의 간격을 두고 행도을 하게 한다.
hubo.set_trace("blue")#휴보의 모든 행동자취에 파란색으로 칠한다

def turn_right():#휴보가 오른쪽으로 돌게 하는 함수를 만든다
    hubo.turn_left()
    hubo.turn_left()#왼쪽으로 총 3번 돌아 결과적으로 오른쪽으로 돌겠금 했다
    hubo.turn_left()
def turn_back():
    hubo.turn_left()
    hubo.turn_left()
while not hubo.front_is_clear():#휴보의 앞에 벽이 없을 때까지 왼쪽으로 돈다
    hubo.turn_left()
hubo.move()#짜놓은 코드메 맟춰서 미리 앞으로 움직여둔다
while not hubo.on_beeper():#휴보가 비퍼를 만나기 전까지 아래 조건문을 반복한다
    if hubo.right_is_clear():#오른쪽에 벽이 없을때 오른쪽으로 돌고 앞으로 이동시킨다
        turn_right()#오른쪽으로 돈다
        hubo.move()#앞으로 간다
    elif hubo.front_is_clear():#앞에 벽이 없을 때 앞으로 이동한다
        hubo.move()#앞으로 간다
    else:
        turn_back()#오른쪽과 앞쪽에 벽이 있을 때, 즉 골목에 있을 때 빠져나오기 위해 왼쪽으로 돈다