import cv2

KENDO_SKELETON_CONNECTIONS = [
    ("left_shoulder", "right_shoulder"),
    ("left_shoulder", "left_elbow"),
    ("left_elbow", "left_wrist"),
    ("right_shoulder", "right_elbow"),
    ("right_elbow", "right_wrist"),
    ("left_shoulder", "left_hip"),
    ("right_shoulder", "right_hip"),
    ("left_hip", "right_hip"),
]

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


def draw_skeleton(frame, points, connections, color=(0, 255, 0)):
    for start_name, end_name in connections:
        if start_name not in points:
            continue
        if end_name not in points:
            continue

        start_point = points[start_name]
        end_point = points[end_name]

        draw_line(frame, start_point, end_point, color=color)

    for point in points.values():
        draw_point(frame, point, color=color)

    return frame


def draw_kendo_skeleton(frame, points, color=(0, 255, 0)):
    return draw_skeleton(
        frame,
        points,
        KENDO_SKELETON_CONNECTIONS,
        color=color,
    )
