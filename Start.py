import Plot
from ConvexHull import ConvexHull


def run():
    n = 10
    i = 0
    dictionary = {}

    while i < n:
        dictionary[i] = []
        hull = ConvexHull(n).hull_list
        dictionary[i] = hull

        i += 1

    hull_list = dictionary

    Plot.Create(hull_list)
