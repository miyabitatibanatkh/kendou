
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