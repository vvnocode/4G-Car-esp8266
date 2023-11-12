import ujson
import enums
import led
import servo
import motor


def detail(topic, msg):
    # 解析报文
    json_data = ujson.loads(msg)
    print(json_data)
    event = json_data.get("event")
    data = json_data.get("data")
    # 处理事件
    if event == enums.LED:
        led.control_led(data)
    elif event == enums.TURN:
        servo.turn_percent(data)
    elif event == enums.RUN:
        motor.run_percent(data)
    elif event == enums.LIGHT:
        print()
