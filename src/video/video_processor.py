from pathlib import Path

from src.analysis.frame_processor import process_detected_frame
from src.pose.detector import detect_pose
from src.video.reader import get_video_properties, open_video, release_video
from src.video.writer import create_video_writer, release_writer, write_frame


def process_video(input_path, output_path, detector):
    cap = open_video(input_path)
    writer = None
    processed_frame_count = 0

    try:
        properties = get_video_properties(cap)

        writer = create_video_writer(
            output_path=output_path,
            fps=properties["fps"],
            width=properties["width"],
            height=properties["height"],
        )

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            result = detect_pose(detector, frame)
            processed_frame, _ = process_detected_frame(frame, result)
            write_frame(writer, processed_frame)
            processed_frame_count += 1

    finally:
        release_video(cap)

        if writer is not None:
            release_writer(writer)

    return {
        "input_path": str(Path(input_path)),
        "output_path": str(Path(output_path)),
        "processed_frame_count": processed_frame_count,
    }