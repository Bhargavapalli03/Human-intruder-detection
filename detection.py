import cv2
import config
from detector import detect_persons
from roi import draw_restricted_zone, is_intruder, get_center
from alert import trigger_alert
from face_auth import is_authorized


def main():
    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        persons = detect_persons(frame)
        draw_restricted_zone(frame)

        for box in persons:
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)
            center = get_center(box)

            if is_intruder(center):
                person_region = frame[y1:y2, x1:x2]
                authorized = is_authorized(person_region)

                if not authorized:
                    cv2.putText(frame,
                                "INTRUDER ALERT!",
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 0, 255),
                                2)
                    trigger_alert(frame)
                else:
                    cv2.putText(frame,
                                "Authorized Person",
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 255, 0),
                                2)
        cv2.imshow("Human Intruder Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()