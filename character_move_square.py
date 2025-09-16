import math
from pico2d import*

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

c_x=400
c_y=90
def minus_move_character(x, speed):
    return x - speed

def plus_move_character(x,speed):
    return x+speed

sg =0
rogic =0
char_speed =2

while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(c_x,c_y)
    if rogic ==0:
        if sg==0:
            c_x=plus_move_character(c_x,char_speed)
            if c_x > 780:
                sg =1
        elif sg ==1:
            c_y=plus_move_character(c_y,char_speed)
            if c_y > 550:
                sg = 2
        elif sg ==2:
            c_x=minus_move_character(c_x,char_speed)
            if c_x < 20:
                sg = 3
        elif sg ==3:
            c_y=minus_move_character(c_y,char_speed)
            if c_y <92:
                sg =0

    elif rogic ==1:
        c_y = plus_move_character(c_y,char_speed)
        c_x = 400 - math.sin(c_y-90/360 * 2 * math.pi)
    if(c_x==400 and c_y==90):
        if rogic==0:
            rogic =1
            sg =0
        else:
            rogic=0
            sg =0
    delay(0.01)

