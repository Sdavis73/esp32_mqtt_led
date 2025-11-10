import network
import time
from machine import Pin, unique_id
import ubinascii
from umqtt.robust import MQTTClient

# Wi-Fi credentials
SSID = "DDavis2470_2.4G"
PASSWORD = "Passion1298"

# MQTT topics
command_topic = b"wyohack/sterling/led/command"
status_topic = b"wyohack/sterling/led/status"

# LED setup
led = Pin(2, Pin.OUT)

# Wi-Fi connection
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# MQTT message callback
def on_message(topic, msg):
    msg = msg.decode().strip().upper()
    print("Received message:", msg)
    if msg == "ON":
        led.on()
        client.publish(status_topic, b"ON")
        print("LED turned ON")
    elif msg == "OFF":
        led.off()
        client.publish(status_topic, b"OFF")
        print("LED turned OFF")

# MQTT connection
def mqtt_connect():
    client_id = b"esp32_led_" + ubinascii.hexlify(unique_id())
    client = MQTTClient(client_id, "broker.hivemq.com")
    client.set_callback(on_message)
    client.connect()
    client.subscribe(command_topic)
    print("Connected to MQTT broker and subscribed to topic.")
    return client

# Main loop
def main():
    connect_wifi(SSID, PASSWORD)
    global client
    client = mqtt_connect()
    while True:
        client.check_msg()
        time.sleep(1)

# Run the program
main()

