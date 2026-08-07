
# Calculate the midpoint between two points in 2D space
def midpoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    xm = (point1[0] + point2[0]) / 2
    ym = (point1[1] + point2[1]) / 2
    return (xm, ym)


# Calculate the Euclidean distance between two points in 2D space
def distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx ** 2 + dy ** 2) ** 0.5


# Calculate the angle formed by three points (pointA, pointB, pointC) in degrees.
def angle_between_three_points(pointA: tuple[float, float], pointB: tuple[float, float], pointC: tuple[float, float]) -> float:
    import math

    # rule: a⋅b=ax​bx​+ay​by​=∥a∥∥b∥cosθ
    vectorBA = (pointA[0] - pointB[0], pointA[1] - pointB[1])
    vectorBC = (pointC[0] - pointB[0], pointC[1] - pointB[1])

    dot_product = vectorBA[0] * vectorBC[0] + vectorBA[1] * vectorBC[1]
    magnitudeBA = (vectorBA[0] ** 2 + vectorBA[1] ** 2) ** 0.5
    magnitudeBC = (vectorBC[0] ** 2 + vectorBC[1] ** 2) ** 0.5

    if magnitudeBA == 0 or magnitudeBC == 0:
        raise ValueError("One of the vectors has zero magnitude, cannot calculate the angle.")

    cos_angle = dot_product / (magnitudeBA * magnitudeBC)
    cos_angle = max(-1, min(1, cos_angle))  # Clamp the value to [-1, 1]
    angle_rad = math.acos(cos_angle)
    angle_deg = math.degrees(angle_rad)
    return angle_deg