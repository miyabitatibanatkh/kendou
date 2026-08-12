import math
from src.analysis.kendo_metrics import (
    calculate_body_lean_angle,
    calculate_elbow_angle,
    calculate_hand_center,
    calculate_shoulder_angle,
)

def test_calculate_elbow_angle():
    shoulder = (0,0)
    elbow = (1,0)
    wrist = (1,1)

    assert math.isclose(calculate_elbow_angle(shoulder, elbow, wrist), 90.0)


def test_calculate_shoulder_angle():
    hip = (0,0)
    shoulder = (1,0)
    elbow = (1,1)

    assert math.isclose(calculate_shoulder_angle(hip, shoulder, elbow), 90.0)


def test_calculate_body_lean_angle():
    shoulder_midpoint = (1, 2)
    hip_midpoint = (0, 0)

    assert math.isclose(
        calculate_body_lean_angle(shoulder_midpoint, hip_midpoint),
        math.degrees(math.atan2(1, 2)),
        abs_tol=0.001,
    )


def test_calculate_hand_center():
    left_wrist = (0, 2)
    right_wrist = (2, 4)

    assert calculate_hand_center(left_wrist, right_wrist) == (1.0, 3.0)
