import cv2
import serial
import time

ser = serial.Serial('COM9', 9600, timeout=1)
time.sleep(2)  

def capture_image():
    cap = cv2.VideoCapture(0) 
    ret, frame = cap.read()
    if ret:
        filename = f"capture_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[✓] Image saved: {filename}")
    else:
        print("[X] Failed to capture image")
    cap.release()

print("Listening for motion...")

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()
        if "Motion Detected! Capturing Image..." in line:
            print("[!] Motion Detected! Capturing Image...")
            capture_image()
