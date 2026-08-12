from src.analysis.geometry import angle_between_three_points, angle_from_vertical

def calculate_elbow_angle(shoulder, elbow, wrist):
    return angle_between_three_points(shoulder, elbow, wrist)


def calculate_shoulder_angle(hip, shoulder, elbow):
    return angle_between_three_points(hip, shoulder, elbow)