from types import SimpleNamespace
from src.pose.landmarks import get_landmark


def test_get_landmark_returns_none_for_invaild_index():
    result  = SimpleNamespace(
        pose_landmarks = [[object(), object()]]
    )

    assert get_landmark(result, -1) is None

    assert get_landmark(result, 2) is None
