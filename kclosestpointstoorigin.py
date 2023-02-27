import math
import heapq

class Item:
    def __init__(self, distance, index):
        self.distance = distance
        self.index = index
    
    def __lt__(self, item):
        return (self.distance < item.distance)

def get_distance_from_origin(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def k_closest(points, k):

    items_list = []
    for i, point in enumerate(points):
        item = Item()
        item.index = i
        item.distance = get_distance_from_origin(point)
        items_list.append(item)

    heapq.heapify(items_list)
    k_closest_points = []
    while k > 0:
        item = heapq.heappop(items_list)
        k_closest_points.append(points[item.index])

    return k_closest_points
