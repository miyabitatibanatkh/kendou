def create_metric_row(frame_index, timestamp_ms, metrics):
    """
    """
    row = {"frame_index": frame_index, "timestamp_ms": timestamp_ms}

    if metrics is None:
        row.update(
            {
                "left_elbow_angle": None,
                "right_elbow_angle": None,
                "left_shoulder_angle": None,
                "right_shoulder_angle": None,
                "body_lean_angle": None,
                "hand_center_x": None,
                "hand_center_y": None,
                "hand_center_offset": None,
                "hand_height_offset": None,
            }
       )

        return row

    hand_center = metrics.get("hand_center")

    row.update(
        {
            "left_elbow_angle": metrics.get("left_elbow_angle"),
            "right_elbow_angle": metrics.get("right_elbow_angle"),
            "left_shoulder_angle": metrics.get("left_shoulder_angle"),
            "right_shoulder_angle": metrics.get("right_shoulder_angle"),
            "body_lean_angle": metrics.get("body_lean_angle"),
            "hand_center_x": hand_center[0] if hand_center is not None else None,
            "hand_center_y": hand_center[1] if hand_center is not None else None,
            "hand_center_offset": metrics.get("hand_center_offset"),
            "hand_height_offset": metrics.get("hand_height_offset"),
        }
    )

    return row

    