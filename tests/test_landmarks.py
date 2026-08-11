from types import SimpleNamespace
from src.pose.landmarks import get_landmark, landmark_to_pixel


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
