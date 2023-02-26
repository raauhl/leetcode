import math
import heapq

def get_distance_from_origin(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def k_closest(points, k):

    distances = []
    for i, point in enumerate(points):
        distance_from_origin = get_distance_from_origin(point)
        distances.append([])

    heap = heapq.
