
import math

from src.analysis.geometry import (
    midpoint, 
    distance,
    angle_between_three_points,
    angle_from_vertical
    )


# Test cases for the geometry functions
def test_midpoint():
    # Test case 1: Midpoint of (0, 0) and (2, 2)
    assert midpoint((0, 0), (2, 2)) == (1.0, 1.0)

    # Test case 2: Midpoint of (-1, -1) and (1, 1)
    assert midpoint((-1, -1), (1, 1)) == (0.0, 0.0)

    # Test case 3: Midpoint of (3, 4) and (5, 6)
    assert midpoint((3, 4), (5, 6)) == (4.0, 5.0)

    # Test case 4: Midpoint of (0, 5) and (10, 15)
    assert midpoint((0, 5), (10, 15)) == (5.0, 10.0)

    # Test case 5: Midpoint of (-3, -4) and (-7, -8)
    assert midpoint((-3, -4), (-7, -8)) == (-5.0, -6.0)


# Test cases for the distance function
def test_distance():
    # Test case 1: Distance between (0, 0) and (3, 4)
    assert distance((0, 0), (3, 4)) == 5.0

    # Test case 2: Distance between (-1, -1) and (1, 1)
    assert distance((-1, -1), (1, 1)) == math.sqrt(8)

    # Test case 3: Distance between (2, 3) and (5, 7)
    assert distance((2, 3), (5, 7)) == 5.0

    # Test case 4: Distance between (0, 0) and (0, 0)
    assert distance((0, 0), (0, 0)) == 0.0

    # Test case 5: Distance between (-2, -3) and (-5, -7)
    assert distance((-2, -3), (-5, -7)) == 5.0


# Test cases for the angle_between_three_points function
def test_angle_between_three_points():
    # Test case 1: Angle between points (0, 0), (1, 0), (1, 1)
    assert math.isclose(angle_between_three_points((0, 0), (1, 0), (1, 1)), 90.0)

    # Test case 2: Angle between points (0, 0), (1, 1), (2, 2)
    assert math.isclose(angle_between_three_points((0, 0), (1, 1), (2, 2)), 180.0, abs_tol=0.001)

    # Test case 3: Angle between points (0, 0), (1, 1), (2, 0)
    assert math.isclose(angle_between_three_points((0, 0), (1, 1), (2, 0)), 90.0)

    # Test case 4: Angle between points (-1, -1), (-2, -2), (-3, -3)
    assert math.isclose(angle_between_three_points((-1, -1), (-2, -2), (-3, -3)), 180.0, abs_tol=0.001)

    # Test case 5: Angle between points (0, 0), (1, -1), (2, -2)
    assert math.isclose(angle_between_three_points((0, 0), (1, -1), (2, -2)), 180.0, abs_tol=0.001)


# Test cases for the angle_from_vertical function
def test_angle_from_vertical():
    # Test case 1: Angle from vertical for points (0, 0) and (0, 1)
    assert math.isclose(angle_from_vertical((0, 0), (0, 1)), 0.0)

    # Test case 2: Angle from vertical for points (0, 0) and (1, 0)
    assert math.isclose(angle_from_vertical((0, 0), (1, 0)), 90.0)

    # Test case 3: Angle from vertical for points (1, 1) and (2, 2)
    assert math.isclose(angle_from_vertical((1, 1), (2, 2)), 45.0)

    # Test case 4: Angle from vertical for points (-1, -1) and (-2, -3)
    assert math.isclose(angle_from_vertical((-1, -1), (-2, -3)), math.degrees(math.atan2(1, 2)), abs_tol=0.001)

    # Test case 5: Angle from vertical for points (3, 4) and (5, 6)
    assert math.isclose(angle_from_vertical((3, 4), (5, 6)), math.degrees(math.atan2(2, 2)), abs_tol=0.001)

