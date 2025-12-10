# Gesture Control Using Arduino & Python

This project allows you to control your computer using **hand gestures** without touching the keyboard or mouse.  
It uses **two Ultrasonic Sensors + Arduino UNO + Python (PyAutoGUI)** to perform actions such as:

- Scroll Up / Scroll Down
- Switch Browser Tabs
- Play / Pause Videos
- Adjust Volume
- Task Switching

---

## 🚀 Features
- Completely touchless computer control  
- Uses affordable Ultrasonic Sensors  
- Python script converts hand gestures into actions  
- Works on any Windows laptop  
- Simple, portable and low-cost

---

## 🛠 Components Required
- Arduino UNO
- Ultrasonic Sensor HC-SR04 (x2)
- Jumper Wires
- USB Cable
- Laptop with Python installed

---

## 🔌 Circuit Diagram
Two ultrasonic sensors mounted on top corners of laptop screen.  
Right sensor = Scrolling / Tab next  
Left sensor = Previous tab / Play pause  
Both together = Task switch

---

## 💻 Arduino Code
Arduino reads distances from both ultrasonic sensors and sends them to Python.

Code file: **gesture_control.ino**

---

## 🐍 Python Code
Python receives distance values and performs actions using `pyautogui`.

Code file: **gesture_control.py**

---

## ▶️ How to Run
### 1. Upload Arduino Code  
Open Arduino IDE -> Upload `gesture_control.ino`

### 2. Install Python Libraries  

### 3. Run Python Script  

Move your hand in front of the sensors and enjoy gesture control!

---

## ✨ Applications
- Education  
- VR/AR Development  
- Accessibility for disabled users  
- Human-Computer Interaction (HCI)  
- Robotics projects

---

## 👩‍💻 Author
**Manisha Nagar**


