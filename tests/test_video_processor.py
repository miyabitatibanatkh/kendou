from types import SimpleNamespace

import cv2
import numpy as np

from src.video.video_processor import process_video


def create_test_video(video_path, frame_count=3, width=320, height=240, fps=10):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(video_path), fourcc, fps, (width, height))

    for _ in range(frame_count):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        writer.write(frame)

    writer.release()


def create_fake_pose_result():
    landmarks = [SimpleNamespace(x=0, y=0, visibility=1.0) for _ in range(33)]

    landmarks[11] = SimpleNamespace(x=0.3, y=0.2, visibility=1.0)
    landmarks[12] = SimpleNamespace(x=0.7, y=0.2, visibility=1.0)
    landmarks[13] = SimpleNamespace(x=0.25, y=0.4, visibility=1.0)
    landmarks[14] = SimpleNamespace(x=0.75, y=0.4, visibility=1.0)
    landmarks[15] = SimpleNamespace(x=0.2, y=0.6, visibility=1.0)
    landmarks[16] = SimpleNamespace(x=0.8, y=0.6, visibility=1.0)
    landmarks[23] = SimpleNamespace(x=0.35, y=0.8, visibility=1.0)
    landmarks[24] = SimpleNamespace(x=0.65, y=0.8, visibility=1.0)

    return SimpleNamespace(pose_landmarks=[landmarks])


def test_process_video_writes_output_video(tmp_path, monkeypatch):
    input_path = tmp_path / "input.mp4"
    output_path = tmp_path / "output.mp4"
    detector = object()

    create_test_video(input_path, frame_count=3)

    def fake_detect_pose(detector, frame, timestamp_ms):
        return create_fake_pose_result()

    monkeypatch.setattr(
        "src.video.video_processor.detect_pose",
        fake_detect_pose,
    )

    result = process_video(input_path, output_path, detector)

    assert result["processed_frame_count"] == 3
    assert result["input_path"] == str(input_path)
    assert result["output_path"] == str(output_path)
    assert output_path.exists()

    cap = cv2.VideoCapture(str(output_path))
    assert cap.isOpened()
    assert int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) == 3
    cap.release()