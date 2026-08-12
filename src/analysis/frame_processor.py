from src.analysis.kendo_metrics import calculate_metrics_from_points
from src.pose.landmarks import extract_kendo_points
from src.visualization.overlay import draw_kendo_analysis_overlay


def process_detected_frame(frame, result):
    frame_height, frame_width = frame.shape[:2]

    points = extract_kendo_points(
        result,
        frame_width=frame_width,
        frame_height=frame_height,
    )

    if points is None:
        return frame, None

    metrics = calculate_metrics_from_points(points)
    draw_kendo_analysis_overlay(frame, points, metrics)

    return frame, metrics