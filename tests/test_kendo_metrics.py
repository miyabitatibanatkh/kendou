import math
from src.analysis.kendo_metrics import (
    calculate_body_lean_angle,
    calculate_elbow_angle,
    calculate_hand_center,
    calculate_hand_center_offset,
    calculate_metrics_from_points,
    calculate_shoulder_angle,
    calculate_hand_height_offset,
    calculate_frame_metrics,
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


def test_calculate_hand_center_offset():
    hand_center = (7, 3)
    body_center = (5, 3)

    assert calculate_hand_center_offset(hand_center, body_center) == 2


def test_calculate_hand_center_offset_left_side():
    hand_center = (3, 3)
    body_center = (5, 3)

    assert calculate_hand_center_offset(hand_center, body_center) == -2


def test_calculate_hand_height_offset_above_shoulder():
    hand_center = (5, 3)
    shoulder_midpoint = (5, 8)

    assert calculate_hand_height_offset(hand_center, shoulder_midpoint) == 5


def test_calculate_hand_height_offset_below_shoulder():
    hand_center = (5, 10)
    shoulder_midpoint = (5, 8)

    assert calculate_hand_height_offset(hand_center, shoulder_midpoint) == -2


def test_calculate_frame_metrics_returns_expected_keys():
    metrics = calculate_frame_metrics(
        left_shoulder=(0, 2),
        right_shoulder=(2, 2),
        left_elbow=(0, 1),
        right_elbow=(2, 1),
        left_wrist=(0, 0),
        right_wrist=(2, 0),
        left_hip=(0, 4),
        right_hip=(2, 4),
    )

    assert set(metrics.keys()) == {
        "left_elbow_angle",
        "right_elbow_angle",
        "left_shoulder_angle",
        "right_shoulder_angle",
        "body_lean_angle",
        "hand_center",
        "hand_center_offset",
        "hand_height_offset",
    }

    assert metrics["hand_center"] == (1.0, 0.0)
    assert metrics["hand_center_offset"] == 0.0
    assert metrics["hand_height_offset"] == 2.0


def test_calculate_metrics_from_points_returns_frame_metrics():
    points = {
        "left_shoulder": (0, 2),
        "right_shoulder": (2, 2),
        "left_elbow": (0, 1),
        "right_elbow": (2, 1),
        "left_wrist": (0, 0),
        "right_wrist": (2, 0),
        "left_hip": (0, 4),
        "right_hip": (2, 4),
    }

    metrics = calculate_metrics_from_points(points)

    assert metrics["hand_center"] == (1.0, 0.0)
    assert metrics["hand_center_offset"] == 0.0
    assert metrics["hand_height_offset"] == 2.0