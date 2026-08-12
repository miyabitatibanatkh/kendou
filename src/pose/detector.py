from pathlib import Path
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import mediapipe as mp

# Create a pose landmarker instance
def create_pose_detector(model_path: Path):
    base_options = python.BaseOptions(model_asset_path=str(model_path))

    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
    )

    return vision.PoseLandmarker.create_from_options(options)


# Detect pose in a frame
def detect_pose(detector, frame, timestamp_ms: int = 0):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    return detector.detect_for_video(mp_image, timestamp_ms)
