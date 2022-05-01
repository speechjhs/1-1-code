from cs1robots import *"처음에 hubo관련 모듈을 가지고 온다
load_world("worlds/amazing5.wld")"우리가 탈출할 worlds/amzing5.wld라는 맵을 불러온다
hubo = Robot(beepers=1, avenue=2, street=1)"처음에 휴보를 소환을 할 때 (2,1)에서 소환을 하고 비퍼를 한 개 지니게 한다
hubo.set_pause(1)"모든 행동을 할 때 마다 1초의 간격을 두고 행동을 한다
hubo.set_trace("blue")"휴보가 지나가는 모든 동선을 파란 색으로 자취를 남긴다. 이때 휴보가 도는 과정 또한 자취가 남는다.
hubo.drop_beeper()"휴보가 생성 되고 비퍼를 하나 내려 놓는다/
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
" def turn_right은 현재 휴보의 모듈에서 휴보가 오른쪽으로 회전하는 함수가 없기 때문에 우리가 임의로 오른쪽으로 돌도록 함수를 선안한다.
"이떄 결과적으로는 오른쪽을 돌지만 그 과정에서는 왼쪽으로 3번을 돈다.
while not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
"처음에 휴보가 벽을 마주보고 있을 수도 있는 상황을 고려해 휴보가 벽을 오른쪽에 두고 움직이도록 짰다
"이때 while문을 설명하자면 휴보가 벽을 마주보고 있지 않을 때까지 왼쪽으로 돌게 하고, 앞에 벽이 없어지는 순간 while을 탈출해 앞으로 이동한다
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()"오른쪽에 벽이 없을 때, 즉 코너에 있을때 오른쪽으로 돌고 앞으로 가도록 한다
    elif hubo.front_is_clear():
        hubo.move()"앞에 있는 조건문이 0일때, 즉 오른쪽에 벽이 있을 때 앞으로 가도록 한다
    else:
        hubo.turn_left()"오른쪽에도 벽이 있고, 앞에도 벽이 있을 때 왼쪽으로 돌도록 한다.
"미로 탈출할 때 벽을 오른쪽으로 두고 움직이도록 설정했다
"그래서 코드를 짤 때도 항상 벽이 오른쪽에 두고 움직이도록 코드를 짰다
"""
오른쪽으로 돌고 전진(1):
    if 충돌시:
        왼쪽으로 회전
    안 충돌하면 다시(1)반복 
이 과정을 다시 비퍼를 만날 때 까지 반복하면, 탈출할 것이라 생각해 이를 바탕으로 코드를 짰다.   
"""