from deepface import DeepFace
import cv2
import os

AUTHORIZED_FOLDER = "authorized faces"

def is_authorized(frame):
    try:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for filename in os.listdir(AUTHORIZED_FOLDER):
            image_path = os.path.join(AUTHORIZED_FOLDER, filename)
            result = DeepFace.verify(
                img1_path=rgb_frame,
                img2_path=image_path,
                model_name="Facenet",
                detector_backend="opencv",
                enforce_detection=False
            )

            if result["distance"] < 0.7:
                return True
        return False
    
    except Exception as e:
        print("Face auth error:", e)
        return False