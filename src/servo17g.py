from machine import Pin, PWM


class Servo:
    def __init__(self, pin):
        # 创建一个PWM对象
        self.servo = PWM(Pin(pin))

        # 舵机参数
        self.frequency = 300  # 舵机的频率 300Hz
        self.period = 1000 * 1000 / self.frequency  # 舵机的周期 μs
        self.min_us = 500  # 最小脉冲宽度 μs
        self.max_us = 2500  # 最大脉冲宽度 μs
        self.min_angle = 0  # 最小角度
        self.max_angle = 200  # 最大角度

        # 设置舵机的频率
        self.servo.freq(self.frequency)

    def set_angle(self, angle):
        # 将角度转换为脉冲宽度
        us = self.map_angle(angle, self.min_angle, self.max_angle, self.min_us, self.max_us)
        print("脉冲：", us)
        # 将脉冲宽度转换为duty
        duty = int(us / self.period * 1023)
        print("占空比：", us / self.period)
        print("duty：", duty)

        # 设置舵机的脉冲宽度
        self.servo.duty(duty)

    def map_angle(self, x, in_min, in_max, out_min, out_max):
        # 将一个数从一个范围映射到另一个范围
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min

