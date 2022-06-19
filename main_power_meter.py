import json
import time
import mqtt
import wifi
from machine import RTC, Pin, I2C
from ina219 import INA219
from logging import INFO

# This template assumes the following file setup
# - main.py
# - wifi.py
# - mqtt.py
# - cert
#    | - cert.der
#    | - private.der
#    | - wifi_passwds.txt
SHUNT_OHMS = 0.1
i2c = I2C(-1, Pin(22), Pin(21))
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

MQTT_TOPIC = "pmdyn"


def convert_to_iso(datetime):
    y, m, d, _, h, mi, s, _ = datetime
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y, m, d, h, mi, s)

def publish_environment_data(mqtt_client):

    iso_timestamp = convert_to_iso(RTC().datetime())

    message = {"Voltage": ina.voltage(),
               "Current": ina.current(),
               "Power": ina.power(),
               "timestamp": iso_timestamp
               }
    mqtt_client.publish(MQTT_TOPIC, json.dumps(message))

def connect_and_publish():
    print("connect wifi and synchronize RTC")
    wifi.connect()
    wifi.synchronize_rtc()

    print("connect mqtt")
    mqtt_client = mqtt.connect_mqtt()

    print("start publishing data")
    while True:
        try:
            publish_environment_data(mqtt_client)
            print("Bus Voltage: %.3f V" % ina.voltage())
            print("Current: %.3f mA" % ina.current())
            print("Power: %.3f mW" % ina.power())
        except Exception as e:
            print(str(e))
        time.sleep(1)


connect_and_publish()
