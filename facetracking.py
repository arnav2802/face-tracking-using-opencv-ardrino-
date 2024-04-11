import cv2
import serial
import time
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)


if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()


ArduinoSerial = serial.Serial('com3', 9600, timeout=0.1)
time.sleep(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    frame = cv2.flip(frame, 1) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)  
    for x, y, w, h in faces:
        
        string = 'X{0:d}Y{1:d}'.format((x + w // 2), (y + h // 2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
      
        cv2.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)


    cv2.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                  (640 // 2 + 30, 480 // 2 + 30),
                  (255, 255, 255), 3)

    cv2.imshow('Face Detection', frame)

   
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
