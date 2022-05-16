import math #подключил для нахождения квадрата числа и извличения квадратного корня

class Point2D:
    __counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__counter += 1

    @classmethod
    def getter(cls):
        return cls.__counter

    def distance(self, point):
        distance_beetwen_point = math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2))
        return distance_beetwen_point

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        distance_beetwen_point = math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2) + math.pow((point.z - self.z), 2))
        return distance_beetwen_point