import math
from src.analysis.kendo_metrics import calculate_elbow_angle

def test_calculate_elbow_angle():
    shoulder = (0,0)
    elbow = (1,0)
    wrist = (1,1)

    assert math.isclose(calculate_elbow_angle(shoulder, elbow, wrist), 90.0)