import numpy as np
from src.visualization.overlay import (draw_point,draw_line)

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