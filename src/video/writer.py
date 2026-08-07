import cv2
from pathlib import Path


def create_video_writer(output_path: str | Path, fps: float, width: int, height: int) -> cv2.VideoWriter:
    path = Path(output_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(str(path), fourcc, fps, (width, height))

    if not writer.isOpened():
        writer.release()
        raise ValueError(f"Failed to create a video writer for the file at {output_path}. Check the output path and format.")

    return writer


def write_frame(writer: cv2.VideoWriter, frame: cv2.Mat) -> None:
    writer.write(frame)


def release_writer(writer: cv2.VideoWriter) -> None:
    if writer.isOpened():
        writer.release()
