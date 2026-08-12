from types import SimpleNamespace
import numpy as np

from src.analysis.frame_processor import process_detected_frame


def test_process_detected_frame_draws_overlay_and_returns_metrics():
    frame = np.zeros((500, 1000, 3), dtype=np.uint8)
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

    processed_frame, metrics = process_detected_frame(frame, result)

    assert processed_frame.sum() > 0
    assert metrics is not None
    assert "left_elbow_angle" in metrics


def test_process_detected_frame_returns_none_metrics_when_points_are_missing():
    frame = np.zeros((500, 1000, 3), dtype=np.uint8)
    result = SimpleNamespace(pose_landmarks=[])

    processed_frame, metrics = process_detected_frame(frame, result)

    assert processed_frame is frame
    assert metrics is None