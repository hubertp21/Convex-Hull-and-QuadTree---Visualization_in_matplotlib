import matplotlib.pyplot as plt

from Point import *
from Rectangle import *
from Quadtree import Quadtree
from ConvexHull import draw


class Create:

    def __init__(self, hull_dictionary):
        DPI = 72
        width, height = 100, 100

        points = []
        for each in hull_dictionary.values():

            for point in each:
                points.append(Point(point[0], point[1]))

        domain = Rectangle(Point(width / 2, height / 2), width / 2, height / 2)
        qtree = Quadtree(domain)

        for point in points:
            qtree.insert(point)

        # draw rects
        fig = plt.figure(figsize=(700 / DPI, 500 / DPI), dpi=DPI)
        ax = plt.subplot()
        draw(hull_dictionary, ax)

        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        qtree.draw(ax)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.invert_yaxis()
        plt.tight_layout()
        plt.show()
