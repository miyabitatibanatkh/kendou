from pathlib import Path
import cv2

def open_video(video_path: str | Path) -> cv2.VideoCapture:
    
    path = Path(video_path)
    if not path.exists():
        raise FileNotFoundError(f"The video file at {video_path} does not exist.")

    # TODO: Add error handling for invalid paths or unsupported formats
    
    pass

