
"""img = load_picture("만화 반전.png")
img.show()
w, h = img.size()
print(w,h)
for y in range(h):
    for x in range(w):
        r,g,b = img.get(x,y)
        r,g,b = 255-r, 255-g,255-b
        img.set(x,y,(r,g,b))
img.show()"""
"""
from cs1media import *
threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)
img = load_picture("ho.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b) // 3 # 각 픽셀의 r, g, b 평균값 v 를 얻기
        if v > threshold:
            img.set(x, y, white)
        else:
            img.set(x, y, black)
img.show()"""

"""from cs1robots import *

create_world()
def name(a,b):
    a  = Robot("yellow")
    b = Robot("blue")
    return a,b
    a.set_pause(0.5)
    b.set_pause(0.5)

    a.set_trace("yellow")
    b.set_trace("blue")
name(ami, bo)

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

ami.move()
ami.move()
ami.move()
ami.move()

turn_right(ami)
turn_right(hubo)"""
"""
str_input = int(input())
num_input = str_input
print()
print(num_input ,"inch")
print(num_input*2.54 ,"cm")"""
