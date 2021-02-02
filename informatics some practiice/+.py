import math


class Point:
    def pp(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt(
            (other_point.x - self.x) ** 2
            + (other_point.y - self.y) ** 2)


p1 = Point(2, 5)
p2 = Point(4, 6)
print(p1.dist(p2))