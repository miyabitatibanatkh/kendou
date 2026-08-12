from types import SimpleNamespace
from src.analysis.kendo_metrics import calculate_frame_metrics
from src.pose.landmarks import (get_landmark, 
                                landmark_to_pixel, 
                                is_landmark_visible,
)

def test_get_landmark_returns_none_for_invaild_index():
    result  = SimpleNamespace(
        pose_landmarks = [[object(), object()]]
    )

    assert get_landmark(result, -1) is None

    assert get_landmark(result, 2) is None


def test_landmarks_to_pixel():
    landmark = SimpleNamespace(x = 0.25, y = 0.5)

    pixel = landmark_to_pixel(
        landmark,
        frame_width = 640,
        frame_height = 480,
    )

    assert pixel == (160, 240)

def test_is_landmark_visible():
    landmark = SimpleNamespace(visibility = 0.6)

    assert is_landmark_visible(landmark, min_visibility=0.5) is True

    assert is_landmark_visible(landmark, min_visibility=0.7) is False

    assert is_landmark_visible(None) is False

    landmark_no_visibility = SimpleNamespace()
    assert is_landmark_visible(landmark_no_visibility) is False


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


