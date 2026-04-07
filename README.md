Description of Project:
The current project is the real-time Human Intruder Detection System which employs YOLOv8 and DeepFace. This system detects humans using 
a webcam, identifies if they are authorized or not, and raises an alarm if there is an intruder.

Features:
Real-time human detection
Facial recognition
Image-based alert on Telegram
Image-based alert on Gmail

Requirements:
Python
OpenCV
DeepFace
Requests

Installation:
pip install ultralytics opencv-python deepface requests

Execution Procedure:
Go to the project directory
Modify config.py file:
        Telegram Bot API Key
        Telegram Chat ID
        Gmail Account Username
        Gmail Application Password
Run the application:
        python detection.py
