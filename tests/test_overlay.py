import numpy as np
from src.visualization.overlay import (KENDO_SKELETON_CONNECTIONS, draw_point,draw_line, draw_skeleton)

def test_draw_point_changes_frame_pixel():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    point = (50, 50)
    color = (255, 0, 0)
    radius = 5

    modified_frame = draw_point(frame.copy(), point, color=color, radius=radius)

    # Check that the pixel at the point has changed to the specified color
    assert np.array_equal(modified_frame[50, 50], np.array(color))


def test_draw_line_changes_frame_pixels():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)

    result = draw_line(frame, (10, 10), (90, 10))

    assert result[10, 50].sum() > 0


def test_draw_skeleton_changes_frame_pixels():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)

    points = {
        "left_shoulder": (10, 10),
        "left_elbow": (50, 10),
        "left_wrist": (90, 10),
    }

    connections = [
        ("left_shoulder", "left_elbow"),
        ("left_elbow", "left_wrist"),
    ]

    result = draw_skeleton(frame, points, connections)

    assert result[10, 10].sum() > 0
    assert result[10, 50].sum() > 0
    assert result[10, 90].sum() > 0


def test_kendo_skeleton_connections_include_core_body_lines():
    assert ("left_shoulder", "right_shoulder") in KENDO_SKELETON_CONNECTIONS
    assert ("left_shoulder", "left_elbow") in KENDO_SKELETON_CONNECTIONS
    assert ("left_elbow", "left_wrist") in KENDO_SKELETON_CONNECTIONS
    assert ("right_shoulder", "right_elbow") in KENDO_SKELETON_CONNECTIONS
    assert ("right_elbow", "right_wrist") in KENDO_SKELETON_CONNECTIONS
    assert ("left_hip", "right_hip") in KENDO_SKELETON_CONNECTIONS