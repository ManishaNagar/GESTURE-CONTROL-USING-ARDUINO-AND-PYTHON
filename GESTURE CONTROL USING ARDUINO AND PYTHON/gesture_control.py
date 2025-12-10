# PYTHON PROGRAM FOR HAND GESTURE CONTROL

# This program reads distance values sent by Arduino
# from two ultrasonic sensors (Right & Left).
# Based on the distance, it performs actions like:
#   1. Scroll up : Hand < 15 cm on RIGHT sensor.
#   2. Scroll down : Hand between 15-35 cm from RIGHT sensor.
#   3. Next tabs : Swipe hand fast across RIGHT sensor, hand very far : hand > 40 cm from right ultrasonic sensor.
#   4. Previous tabs : Swipe hand fast across LEFT sensor, hand very far hand > 40 cm from left ultrasonic sensor.
#   5. Play/Pause : If hand suddenly moves from far (>30) to near (<15)
#   6. Task switch : Hands close to both sensors.

# We use:
#   pyserial  -> to connect with Arduino
#   pyautogui -> to control keyboard/mouse actions


import serial
import pyautogui
import time
# for adding time delays

# CONNECTING TO ARDUINO

# Change 'COM3' if your Arduino uses another port.
# To check: Tools -> Port in Arduino IDE.
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for connection to settle

print("Gesture Control Started... Move your hand!")

# To detect sudden movement, we store the last reading
last_left_distance = 100

while True:

    # Read a line from Arduino (example: "25,50" , 25 is left hand's distance from left ultrasonic sensor & 50 is right hand's distance from right ultrasonic sensor.)
    data = arduino.readline().decode().strip()

    # Try to split into two numbers that is left and right
    try:
        right, left = map(int, data.split(","))
    except:
        continue  # If error, skip and read next line


# DEFINING GESTURES BASED ON RIGHT SENSOR

    # Gesture 1: Scroll DOWN (hand near right sensor)
    if 15 < right < 35:
        pyautogui.scroll(-40)   # Negative = scroll down

    # Gesture 2: Scroll UP (hand very close)
    if right < 15:
        pyautogui.scroll(40)    # Positive = scroll up

    # Gesture 3: Next Tab (swipe fast across right sensor)
    if right > 40:
        pyautogui.hotkey("ctrl", "tab")


# DEFINING GESTURES BASED ON LEFT SENSOR


    # Gesture 4: Previous Tab
    if left > 40:
        pyautogui.hotkey("ctrl", "shift", "tab")

    # PLAY / PAUSE GESTURE (LEFT SENSOR MOVES FAST)
    # If hand suddenly moves from far (>30) to near (<15)
    if last_left_distance > 30 and left < 15:
        pyautogui.press("space")      # Play/Pause
        time.sleep(0.4)               # Prevent double trigger

    # Update last distance
    last_left_distance = left

# DEFINING GESTURES BASED ON BOTH SENSORS
    # Gesture 5: Task switch (Alt + Tab)
    # When both sensors detect hand very close
    if left < 20 and right < 20:
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.5)   # Delay to prevent multiple switches
