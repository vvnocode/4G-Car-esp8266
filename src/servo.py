# 舵机
from machine import Pin, PWM
import time

p2 = PWM(Pin(14))
p2.freq(50)

left_max = 5430
middle = 4650
right_max = 3590

def turn(scale):
    if scale > left_max:
        scale = left_max
    elif scale < right_max:
        scale = right_max
    turn_scale = int(scale)
    print(turn_scale)
    p2.duty_u16(turn_scale)

# 百分比转向
def turn_percent(percentum):
    if (not isinstance(percentum, (int)) or percentum == 0):
        print("回正")
        turn(middle)
    # 左
    elif percentum < 0:
        print("左")
        turn((left_max - middle) * (-percentum) / 100 + middle)
    # 右
    else:
        print("右")
        turn(middle - (middle - right_max) * percentum / 100)
