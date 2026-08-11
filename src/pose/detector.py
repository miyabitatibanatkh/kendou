from pathlib import Path
from mediapipe.tasks.python import vision


def create_pose_detector(model_path: Path):
    pose = vision.PoseLandmarker.create_from_model_path(str(model_path))
    return pose 

def detect_pose(detector, frame):
    pass