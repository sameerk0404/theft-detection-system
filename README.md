# Theft Detection System using Arduino and Python

This project uses a PIR motion sensor with an Arduino to detect motion, and a Python script to capture images via a webcam when motion is detected.

## Components Used
- Arduino Uno
- PIR Sensor
- Buzzer
- LED
- USB Cable
- Laptop webcam

## How it Works
1. Motion is detected by the PIR sensor.
2. Arduino sends a signal via serial (USB).
3. A Python script reads the signal and captures an image using the webcam.

## How to Run
1. Upload `motion_detector.ino` to your Arduino.
2. Install python dependencies:
```bash
pip install -r requirements.txt
```
3. Run python script:
```
python python/capture_on_motion.py
