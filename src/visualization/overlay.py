import cv2


def draw_point(frame, point, color=(0, 255, 0), radius=5):
    x, y = point
    cv2.circle(frame, (int(x), int(y)), radius, color, -1)
    return frame