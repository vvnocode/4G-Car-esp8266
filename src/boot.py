import wifi
import mqtt
    
def main():
    wifi.do_connect()
#    _thread.start_new_thread(mqtt.mqtt, ())

if __name__ == "__main__":
    main()
