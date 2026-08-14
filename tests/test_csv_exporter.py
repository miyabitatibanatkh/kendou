from src.export.csv_exporter import create_metric_row


def test_create_metric_row_flattens_metrics():
    metrics = {
        "left_elbow_angle": 120.5,
        "right_elbow_angle": 130.0,
        "left_shoulder_angle": 45.0,
        "right_shoulder_angle": 47.5,
        "body_lean_angle": 3.2,
        "hand_center": (100.0, 200.0),
        "hand_center_offset": -12.0,
        "hand_height_offset": 30.0,
    }

    row = create_metric_row(
        frame_index=10,
        timestamp_ms=333,
        metrics=metrics,
    )

    assert row["frame_index"] == 10
    assert row["timestamp_ms"] == 333
    assert row["left_elbow_angle"] == 120.5
    assert row["hand_center_x"] == 100.0
    assert row["hand_center_y"] == 200.0


def test_create_metric_row_handles_missing_metrics():
    row = create_metric_row(
        frame_index=5,
        timestamp_ms=166,
        metrics=None,
    )

    assert row["frame_index"] == 5
    assert row["timestamp_ms"] == 166
    assert row["left_elbow_angle"] is None
    assert row["hand_center_x"] is None