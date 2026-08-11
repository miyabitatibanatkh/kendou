from pathlib import Path
from mediapipe.tasks.python import vision
import cv2
import mediapipe as mp

# Create a pose landmarker instance
def create_pose_detector(model_path: Path):
    pose = vision.PoseLandmarker.create_from_model_path(str(model_path))
    return pose 


# Detect pose in a frame
def detect_pose(detector, frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    results = detector.detect(mp_image)
    return results
