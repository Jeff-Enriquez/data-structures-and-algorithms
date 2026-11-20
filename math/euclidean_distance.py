import math

def euclidean_distance(x1, x2, y1, y2) -> float | int:
    """ This is a variation of Pythagorean theorem -> a^2 + b^2 = c^2
    Pythagorean theorem is used to calculate the length of a missing side in a right triangle.
    Euclidean distance calculates the distance between two points on a 2D plane, such as a graph.
    Euclidean distance -> distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    """
    distance: float | int = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance