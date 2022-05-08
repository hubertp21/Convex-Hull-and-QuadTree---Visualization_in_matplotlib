from Point import *
from Rectangle import *


class Quadtree:
    def __init__(self, boundary, capacity=1):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        # if the point is in the range of current quadtree
        if not self.boundary.containsPoint(point):
            return False
        # if has not reached capacity
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.divide()
            self.divided = True

        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True

        return False

    def queryRange(self, range):

        found_points = []
        if not self.boundary.intersects(range):
            return []

        for point in self.points:
            if range.containsPoint(point):
                found_points.append(point)

        if self.divided:
            found_points.extend(self.nw.queryRange(range))
            found_points.extend(self.ne.queryRange(range))
            found_points.extend(self.sw.queryRange(range))
            found_points.extend(self.se.queryRange(range))

        return found_points

    def queryRadius(self, range, center):

        found_points = []
        if not self.boundary.intersects(range):
            return []

        for point in self.points:
            if range.containsPoint(point) and point.distanceToCenter(center) <= range.width:
                found_points.append(point)

        if self.divided:
            found_points.extend(self.nw.queryRadius(range, center))
            found_points.extend(self.ne.queryRadius(range, center))
            found_points.extend(self.sw.queryRadius(range, center))
            found_points.extend(self.se.queryRadius(range, center))

        return found_points

    def divide(self):
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.nw = Quadtree(nw)

        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.ne = Quadtree(ne)

        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.sw = Quadtree(sw)

        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.se = Quadtree(se)

    def __len__(self):
        count = len(self.points)
        if self.divided:
            count += len(self.nw) + len(self.ne) + len(self.se) + len(self.sw)
        return count

    def draw(self, ax):

        self.boundary.draw(ax)
        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.sw.draw(ax)
            self.se.draw(ax)
