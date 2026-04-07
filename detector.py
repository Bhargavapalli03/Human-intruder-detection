from ultralytics import YOLO
import config

# Load model once
model = YOLO(config.MODEL_NAME)

def detect_persons(frame):
    persons = []

    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if model.names[cls] == "person" and conf > config.CONFIDENCE_THRESHOLD:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                persons.append((x1, y1, x2, y2))

    return persons