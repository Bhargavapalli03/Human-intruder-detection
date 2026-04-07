import cv2
import config

def draw_restricted_zone(frame):
    if config.RESTRICTED_ZONE is None:
        return

    x1, y1, x2, y2 = config.RESTRICTED_ZONE
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

def get_center(box):
    x1, y1, x2, y2 = box
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    return (cx, cy)

def is_intruder(center):
    if config.RESTRICTED_ZONE is None:
        return True

    x1, y1, x2, y2 = config.RESTRICTED_ZONE
    cx, cy = center
    return x1 < cx < x2 and y1 < cy < y2