# ESP32 MQTT LED Control

This project demonstrates how to control an ESP32's onboard LED using MQTT messages via a public broker. It uses MicroPython, MQTT Explorer, and Thonny IDE for development and testing.

## 🔧 Hardware

- ESP32-S3 board
- Onboard LED (GPIO2)
- Wi-Fi connection

## 📡 MQTT Setup

- **Broker**: `broker.hivemq.com`
- **Port**: `1883`
- **Command Topic**: `wyohack/sterling/led/command`
- **Status Topic**: `wyohack/sterling/led/status`

## 🧠 Message Format

- Messages must be sent in **raw** format (not JSON)
- Valid payloads:
  - `ON` → Turns LED on
  - `OFF` → Turns LED off

## 🖥️ Workflow

1. ESP32 connects to Wi-Fi and MQTT broker
2. Subscribes to `command` topic
3. Listens for `ON`/`OFF` messages
4. Publishes LED status to `status` topic

## 🧪 Demo Video Checklist

- ✅ Thonny REPL shows Wi-Fi and MQTT connection
- ✅ MQTT Explorer publishes `ON` and `OFF`
- ✅ LED responds accordingly
- ✅ Status topic updates with `ON` or `OFF`

## 📂 File

- `main.py`: Final MicroPython script with comments

## 🚀 How to Run

1. Flash `main.py` to ESP32 using Thonny
2. Connect to Wi-Fi
3. Open MQTT Explorer and connect to `broker.hivemq.com`
4. Publish `ON`/`OFF` to `wyohack/sterling/led/command`
5. Observe LED and status topic

## 🧹 Optional `.gitignore`

