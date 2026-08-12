import cv2


def draw_point(frame, point, color=(0, 255, 0), radius=5):
    x, y = point
    cv2.circle(frame, (int(x), int(y)), radius, color, -1)
    return frame


def draw_line(frame, start_point, end_point, color=(0, 255, 0), thickness=2):
    start_x, start_y = start_point
    end_x, end_y = end_point

    cv2.line(
        frame,
        (int(start_x), int(start_y)),
        (int(end_x), int(end_y)),
        color,
        thickness,
    )

    return frame

