import wifi
import mqtt


def main():
    # 联网
    wifi.do_connect()
    # mqtt
    mqtt.subscribe()


if __name__ == "__main__":
    main()
