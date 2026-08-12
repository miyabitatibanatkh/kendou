from src.analysis.geometry import angle_between_three_points, angle_from_vertical

def calculate_elbow_angle(shoulder, elbow, wrist):
    return angle_between_three_points(shoulder, elbow, wrist)