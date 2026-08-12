from types import SimpleNamespace
from src.analysis.kendo_metrics import calculate_frame_metrics
from src.pose.landmarks import (get_landmark, 
                                landmark_to_pixel, 
                                is_landmark_visible,
                                extract_kendo_points,
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


def test_extract_kendo_points_returns_required_pixel_points():
    landmarks = [SimpleNamespace(x=0, y=0, visibility=1.0) for _ in range(33)]

    landmarks[11] = SimpleNamespace(x=0.1, y=0.2, visibility=1.0)
    landmarks[12] = SimpleNamespace(x=0.2, y=0.2, visibility=1.0)
    landmarks[13] = SimpleNamespace(x=0.1, y=0.4, visibility=1.0)
    landmarks[14] = SimpleNamespace(x=0.2, y=0.4, visibility=1.0)
    landmarks[15] = SimpleNamespace(x=0.1, y=0.6, visibility=1.0)
    landmarks[16] = SimpleNamespace(x=0.2, y=0.6, visibility=1.0)
    landmarks[23] = SimpleNamespace(x=0.1, y=0.8, visibility=1.0)
    landmarks[24] = SimpleNamespace(x=0.2, y=0.8, visibility=1.0)

    result = SimpleNamespace(pose_landmarks=[landmarks])

    points = extract_kendo_points(result, frame_width=1000, frame_height=500)

    assert points["left_shoulder"] == (100, 100)
    assert points["right_hip"] == (200, 400)


def test_extract_kendo_points_returns_none_when_required_landmark_is_not_visible():
    landmarks = [SimpleNamespace(x=0, y=0, visibility=1.0) for _ in range(33)]
    landmarks[11] = SimpleNamespace(x=0.1, y=0.2, visibility=0.1)

    result = SimpleNamespace(pose_landmarks=[landmarks])

    points = extract_kendo_points(result, frame_width=1000, frame_height=500)

    assert points is None
