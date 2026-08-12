from src.analysis.geometry import (
    angle_between_three_points, 
    angle_from_vertical,
    midpoint,
    distance    
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