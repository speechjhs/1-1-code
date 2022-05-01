from cs1robots import *#휴보 라이브러리에 있는 모든 함수를 불러온다
load_world("worlds/trash2.wld")#trash1이라는 맵을 불러온다
#load_world("worlds/trash2.wld")로 쓰면 trash2이라는 맵을 불러온다 맞찬가지로 trash2에서도 이 코드는 작동한다

hubo = Robot()#처음 휴보가 생성될 때 (1,1)에서[기본값] 소환되도록 한다
hubo.set_pause(0.01)#모든 행동에 있어서 0.01초식 간격을 두고 행동을 한다
hubo.set_trace("blue")#휴보의 모든 움직임을 파란색으로 기록한다

def turn_back():#왼쪽으로 두번 돌게 해서 결과적으로 휴보가 반대 방향을 보도록 하는 함수이다
    hubo.turn_left()
    hubo.turn_left()

def turn_right():#휴보의 함수에서는 바로 오른쪽으로 돌게 하는 함수가 없어, 왼쪽으로 3번돌아 결과적으로 오른쪽을 보도록 하는 함수이다
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def follow_right_wall():#가장 큰 틀로써 오른쪽 벽을 타고 이동하겠금 하는 함수이다
    if hubo.right_is_clear():#trash1맵은 오른쪽으로 도는 부분이 딱 한 부분있어서 이때 비퍼를 내려 놓겠금한다.
        turn_right()#먼저 오른쪽에 코너가 있다는 걸 상상하고 오른쪽으로 돌고 앞으로 이동, 그 후 뒤돌아 비퍼를 하나 두고 앞으로 전진후 왼쪽을 보게한다
        hubo.move()#이렇게 짜면 오른쪽 코너 하나를 제외하고는 직선으로 오른쪽 벽을 타고 비퍼를 줍는 단순한 과정이 된다
        turn_back()
        hubo.drop_beeper()
        hubo.move()
        hubo.turn_left()
    elif hubo.front_is_clear():#앞에 벽이 없을 때 앞으로 전진하게 해주는 역할이다
        hubo.move()
        if hubo.on_beeper():#앞으로 이동한 후에 비퍼가 있다면 줍는다
            hubo.pick_beeper()#여기서 if문과move의 순서를 바꿔도 결과는 바뀌지 않는다
    else:
        hubo.turn_left()#오른쪽에 벽이 있고 앞에도 벽에도 있는 경우 왼쪽으로 돌도록한다.
    """
    else:
        turn_back()#여기서 앞에 있는 turn_left 대신에 사용할 수 있다.
        #그렇게 되면 follow_right_wall() 함수를 콜하는 횟수를 줄일 수 있다 
    """
while not hubo.carries_beepers():#처음에 휴보가 비퍼를 안 가지고 있기 때문에 비퍼를 가지는 순간 탈출하도록 한다
    follow_right_wall()#아래while문을 실행하기 위해서 이 while문을 작성했다
while hubo.carries_beepers():#휴보가 비퍼를 다 드랍할 때까지 follow_right_wall를 하게 한다
    follow_right_wall()
# 마지막으로 이 코드를 작성하면서 아쉬웠던 부분은 아직 hubo.get.pos()[]의 작동 원리를 정확하게 파악하지 못 해서,
#조금 이 맵이 바뀌면 다시 코드를 짜야한다는 점에서 호환성이 약간 떨어진다는 점이 이 코드의 가장큰 단점이라 생각했다
#pos의 작동원리를 알기 위해 강좌qna에도 질문을 남기고 pos를 print하게 해서 어떻게 작동하는지 실험도 많이 했는데 결국은 알지 못 했다
#pos의 작동원리를 정확하게 알았다면 이를 통해 언제든지 내가 원하는 위치에 비퍼를 드랍하도록 해 좀더 융통성이 있는 코드가 될 텐데 그 부분이 아쉬웠다