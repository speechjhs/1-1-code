from cs1robots import *#휴보 관련 함수를 모두 불러온다
load_world("worlds/custom.wld")#custom라는 맵을 불러온다
hubo = Robot(beepers=0, avenue=6, street=3)#휴보가 (1,1)에서 비퍼를 하나 가지고 있는 상태에서 시작하게 한다
hubo.set_pause(0.01)#행동의 간격을 0.01초로 설정한다
hubo.set_trace("blue")# 휴보의 흔적을 파란색으로 기록한다
hubo.turn_left()#처음 설정을 위해 쓴 기본 이동 명령어다
hubo.move()#위에랑 같은 맥랑
def turn_right():#오른쪽으로 휴보가 돌기 위해서 쓴 함수이다
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def ru():#가장 메인이 되는 코드로 계단을 타는 것처럼 해서 이동하게 한다.
    if hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    #위 명령어대로 하면, 명령어 한번 실행시 비퍼를 수집하고, 한계단 올라가는 방식이다.
def cir(a):
    for y in range(a):
        ru()
    hubo.turn_left()
    for y in range(a):
        ru()
    hubo.turn_left()
    for y in range(a):
        ru()
    hubo.turn_left()
    for y in range(a):
        ru()
cir(3)
# cir함수는 휴보가 맵을 봤을때 한 바퀴 돌도록 함수를 짰는데, 그 구간을 4구간으로 나눠서 실행했다.
#그래서 처음엔 오른쪽위, 다음은 왼쪽 위, 왼쪽아래, 오른쪽 아래, 해서 반시계방향으로 돌겠금했다.
#이때 a가 3인 이유는 계단을 3번타면 한 구간이 끝나기 때문에 그렇게 설정했다.
#이때 a값은 매개변수로 설정하고 함수콜할 때 입력받겠금 했다.
hubo.turn_left()
hubo.move()
hubo.move()
#처음 cir(3)이 끝나면 제자리(6,4)에 남기 때문에 다시 한바퀴를 돌기 위해 처음 위치를 잡고자
#위 명령어를 사용했다.
cir(1)
#이번 경우에는 계단을 한번만 올라가서 회전하면 되기 때문에 cir()에 숫자 1을 대입했다.
