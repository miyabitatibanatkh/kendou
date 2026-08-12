from src.analysis.geometry import (
    angle_between_three_points, 
    angle_from_vertical,
    midpoint,
)

def calculate_elbow_angle(shoulder, elbow, wrist):
    return angle_between_three_points(shoulder, elbow, wrist)


def calculate_shoulder_angle(hip, shoulder, elbow):
    return angle_between_three_points(hip, shoulder, elbow)


def calculate_body_lean_angle(shoulder_midpoint, hip_midpoint):
    return angle_from_vertical(hip_midpoint, shoulder_midpoint)


def calculate_hand_center(left_wrist, right_wrist):
    return midpoint(left_wrist, right_wrist)


def calculate_hand_center_offset(hand_center, body_center):
    return hand_center[0] - body_center[0]


def calculate_hand_height_offset(hand_center, shoulder_midpoint):
    return shoulder_midpoint[1] - hand_center[1]


def calculate_frame_metrics(
    left_shoulder,
    right_shoulder,
    left_elbow,
    right_elbow,
    left_wrist,
    right_wrist,
    left_hip,
    right_hip,
):
    shoulder_midpoint = midpoint(left_shoulder, right_shoulder)
    hip_midpoint = midpoint(left_hip, right_hip)
    hand_center = calculate_hand_center(left_wrist, right_wrist)
    body_center = midpoint(shoulder_midpoint, hip_midpoint)

    return {
        "left_elbow_angle": calculate_elbow_angle(left_shoulder, left_elbow, left_wrist),
        "right_elbow_angle": calculate_elbow_angle(right_shoulder, right_elbow, right_wrist),
        "left_shoulder_angle": calculate_shoulder_angle(left_hip, left_shoulder, left_elbow),
        "right_shoulder_angle": calculate_shoulder_angle(right_hip, right_shoulder, right_elbow),
        "hand_center": hand_center,
        "body_lean_angle": calculate_body_lean_angle(shoulder_midpoint, hip_midpoint),
        "hand_center_offset": calculate_hand_center_offset(hand_center, body_center),
        "hand_height_offset": calculate_hand_height_offset(hand_center, shoulder_midpoint),
    }