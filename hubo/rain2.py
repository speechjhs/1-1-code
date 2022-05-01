from cs1robots import *#휴보관련 함수를 모두 불러온다
load_world("worlds/rain2.wld")#rain2라는 맵을 불러온다
hubo = Robot(beepers=10, avenue=2, street=6)#휴보가 2,6에서 20개의 비퍼를 가지고 소환돤다
hubo.set_pause(0.01)#휴보의 모든 행동이 0.01초의 간격을 두고 행동을 한다
hubo.set_trace("blue")#휴보의 모든 행동을 파란색으로 자취를 남긴다
hubo.move()#휴보가 앞으로 움직인다
hubo.drop_beeper()#휴보가 비퍼를 하나 떨어뜨린다
#이때 떨어뜨린 비퍼가 나의 휴보의 움직임의 끝의 기준이 된다
hubo.turn_left()#휴보가 왼쪽으로 돈다
hubo.move()#휴보가 앞으로 움직인다
#초반 휴보의 위치를 설정해준다
def turn_right():#휴보가 과정적으로는 3번 왼쪽으로 이동하지만 결과적으로는 오른쪽으로 이동하게 함수를 쓴다.
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def follow_left_wall():#왼쪽벽을 타고 가겠금한다
    if hubo.left_is_clear():#왼쪽이 비었을때 비퍼를 놓게한다
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()# 여기서 (9,4)쯤에 있는 코너랑 창문이랑 단순히 clear를 이용해서는 구별이 불가능한다
        #창문과 코너 둘다 좌우앞에 벽이 없기 떄문에 새로운 기준을 만들었다.
        # 기준을 생각하던 중 창문같은 경우에는 위 코드를 실행한 뒤에 if문이 성립하기 때문에
        #다시 원상태로 돌려놓고 비퍼를 떨어뜨린다
        if hubo.front_is_clear():
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()
            hubo.drop_beeper()
            hubo.move()
        else:
            turn_right()
            #이때는 아까 말한 코너에 해당되기 때문에 오른쪽으로 돌게 한다
    elif hubo.front_is_clear():
        hubo.move()#휴보앞에 벽이 없다면 앞으로 가게 한다
    else:
        turn_right()
        #앞과 옆이 막힌 경우로 이때는 오른쪽으로 돈다


while not hubo.on_beeper():
    follow_left_wall()
    #모든 작업이 끝날때까지 반복시킨다
hubo.pick_beeper()
#모든 과정이 끝난후에 원래 처음에 비퍼를 놓았던 곳에서 다시 비퍼를 가지고 온다
