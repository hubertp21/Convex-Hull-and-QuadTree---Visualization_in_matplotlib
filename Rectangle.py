

class Rectangle:
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height

        self.west = center.x - width
        self.east = center.x + width
        self.north = center.y - height
        self.south = center.y + height

    def containsPoint(self, point):
        return self.west <= point.x <= self.east and self.north <= point.y <= self.south

    def intersects(self, range):
        return not (range.west > self.east or
                    range.east < self.west or
                    range.north > self.south or
                    range.south < self.north)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)
