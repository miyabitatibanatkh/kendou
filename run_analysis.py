from pathlib import Path

from src.pose.detector import create_pose_detector
from src.video.video_processor import process_video


def main():
    model_path = Path("models/pose_landmarker_heavy.task")
    input_path = Path("data/input/test_input.MOV")
    output_path = Path("data/output/kendo_analysis_output.MOV")

    detector = create_pose_detector(model_path)

    result = process_video(
        input_path=input_path,
        output_path=output_path,
        detector=detector,
    )

    print("Analysis finished")
    print(f"Input: {result['input_path']}")
    print(f"Output: {result['output_path']}")
    print(f"Processed frames: {result['processed_frame_count']}")
    print(f"Detected frames: {result['detected_frame_count']}")
    print(f"Missing pose frames: {result['missing_pose_frame_count']}")
    print(f"FPS: {result['fps']}")
    print(f"Width: {result['width']}")
    print(f"Height: {result['height']}")


if __name__ == "__main__":
    main()