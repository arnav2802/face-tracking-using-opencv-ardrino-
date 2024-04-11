# face-tracking-using-opencv-ardrino

**Face Detection and Tracking**
This repository contains the code for a face detection and tracking system using OpenCV and Arduino. The system uses a webcam to capture video frames, detects faces in the frame using a Haar Cascade classifier, and sends the coordinates of the detected face to an Arduino board via serial communication.The servo motors then move to the corresponding position to track the detected face.

**Features**
Face detection using Haar Cascade classifier
Real-time tracking of detected face using servo motors
Serial communication with Arduino board

**Technologies Used**
OpenCV
Python
Arduino
Servo motors


**Setup**
To use this code for your own face tracking system, follow these steps:

Install OpenCV and Python on your local machine.
Connect two servo motors to your Arduino board and upload the provided Arduino code.
Open the face_tracking.ino file in the Arduino IDE and upload the code to the Arduino board.
Open the face_tracking.py file in a Python IDE and run the script.
Adjust the serial communication settings in the script to match your Arduino board's settings.


**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Contact**
If you have any questions or comments about this project, please contact me at arnav171103@gmail.com.
