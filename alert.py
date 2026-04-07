import os
import cv2
import datetime
import time
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import config
last_alert_time = 0

def send_telegram(image_path):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as img:
        requests.post(url, data={"chat_id": config.TELEGRAM_CHAT_ID}, files={"photo": img})
    print("sent to telegram")

def send_email(image_path):
    try:
        msg = MIMEMultipart()
        msg["Subject"] = "Intruder Alert"
        msg["From"] = config.EMAIL_SENDER
        msg["To"] = config.EMAIL_RECEIVER

        body = f"Intruder detected at {datetime.datetime.now()}"
        msg.attach(MIMEText(body, "plain"))

        with open(image_path, "rb") as f:
            img_data = f.read()
            image = MIMEImage(img_data, name=os.path.basename(image_path))
            msg.attach(image)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent with image")
    except Exception as e:
        print("Email failed:", e) 

def trigger_alert(frame):
    global last_alert_time
    current_time = time.time()

    if current_time - last_alert_time > config.COOLDOWN_TIME:
        os.makedirs(config.SAVE_PATH, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{config.SAVE_PATH}intruder_{timestamp}.jpg"
        print("Intruder detected")
        cv2.imwrite(filename, frame)
        send_telegram(filename)
        send_email(filename)
        last_alert_time = current_time