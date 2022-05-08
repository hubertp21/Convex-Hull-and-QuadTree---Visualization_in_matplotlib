from math import acos
from math import dist
from math import sqrt
from random import sample


class ConvexHull:

    def __init__(self, n):
        for i in range(n):
            list_of_x = sample(range(0, 100), 7)
            list_of_y = sample(range(0, 100), 7)

            entry_list = list(zip(list_of_x, list_of_y))
            entry_list.sort()

            vector_x = entry_list[0][0]
            vector_y = entry_list[0][1]
            list_points_x = []
            list_points_y = []
            for i in range(len(entry_list)):

                if entry_list[i][0] - vector_x < 0:
                    list_points_x.append(-(entry_list[i][0] - vector_x))
                else:
                    list_points_x.append(entry_list[i][0] - vector_x)

                if entry_list[i][1] - vector_y < 0:
                    list_points_y.append(-(entry_list[i][1] - vector_y))
                else:
                    list_points_y.append(entry_list[i][1] - vector_y)

            list_of_points = list(zip(list_points_x, list_points_y))

            x_0 = entry_list[0][0] - vector_x
            y_0 = entry_list[0][1] - vector_y
            degree_list = []
            distance_list = []

            for i in range(1, len(entry_list)):
                x = list_of_points[i][0]
                y = list_of_points[i][1]
                tuple_of_0_0 = (x_0, y_0)
                tuple_of_points = (x, y)
                distance = dist(tuple_of_0_0, tuple_of_points)
                distance_list.append(distance)

                vec_0_x = 0
                vec_0_y = -1

                scalar_product = vec_0_x * x + vec_0_y * y
                length_of_vec_i = sqrt(x * x + y * y)
                value = scalar_product / length_of_vec_i
                alfa = acos(value)
                temp_degrees = (180 * alfa) / 3.14
                if temp_degrees < 0:
                    temp_degrees = -temp_degrees
                degree_list.append(temp_degrees)

            del list_of_points[0]
            list_pom = list(zip(list_of_points, degree_list))
            list_pom.sort(key=lambda x: x[1])
            list_3_elems = list_pom

            final_list = []
            for i in list_3_elems:
                final_list.append(i[0])
            final_list.insert(0, (0, 0))
            final_list.append((0, 0))

            hull_list = []
            for i in range(1, len(final_list) - 1, 1):

                tail = final_list[i - 1]
                medium = final_list[i]
                head = final_list[i + 1]

                xt = tail[0]
                yt = tail[1]
                xm = medium[0]
                ym = medium[1]
                xh = head[0]
                yh = head[1]

                a = (yh - yt) / (xh - xt)
                # b = yh - (a * xh)
                det = xt * yh + xh * ym + xm * yt - xm * yh - xt * ym - xh * yt
                if det < 0:
                    hull_list.append(medium)
                elif det > 0:
                    pass

            hull_list.insert(0, (0, 0))
            hull_list.append((0, 0))

            self.hull_list = hull_list


def draw(hull_dictionary, ax):
    for i in range(1, len(hull_dictionary), 1):
        hull = hull_dictionary[i]
        xs, ys = map(list, zip(*hull))
        ax.fill(xs, ys, c="red")
