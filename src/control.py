import ujson
import enums
from servo17g import Servo
import motor

servo = Servo(0)  # D3


def detail(topic, msg):
    # 解析报文
    json_data = ujson.loads(msg)
    print(json_data)
    event = json_data.get("event")
    data = json_data.get("data")
    # 处理事件
    if event == enums.TURN:
        servo.set_angle(data)
    elif event == enums.RUN:
        motor.run_percent(data)
    elif event == enums.LIGHT:
        print()
