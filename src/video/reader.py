from pathlib import Path
import cv2


def open_video(video_path: str | Path) -> cv2.VideoCapture:
    
    path = Path(video_path)
    if not path.exists():
        raise FileNotFoundError(f"The video file at {video_path} does not exist.")

    cap = cv2.VideoCapture(str(path))  
    if not cap.isOpened():
        cap.release()
        raise ValueError(f"Failed to open the video file at {video_path}. It may be in an unsupported format.")    
    return cap

def read_first_frame(cap: cv2.VideoCapture) -> cv2.Mat:
    ret, frame = cap.read()
    if not ret:
        raise ValueError("Failed to read a frame from the video. The video may be corrupted or in an unsupported format.")

    return frame
