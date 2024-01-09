import numpy as np


                                                                #########################################
                                                                #                                       #
                                                                #       ESTIMATING INTERSECTION         #
                                                                #                                       #
                                                                #########################################


def convert_to_radians(degrees):
    return np.radians(degrees)

def calculate_direction_vector(azimuth_rad, elevation_rad):
    return np.array([
        np.sin(azimuth_rad) * np.cos(elevation_rad),
        np.cos(azimuth_rad) * np.cos(elevation_rad),
        np.sin(elevation_rad)
    ])

def find_intersection_point(p1, d1, p2, d2):
    # Check if lines are parallel
    if np.all(np.cross(d1, d2) == 0):
        # Lines are parallel, find the point of closest approach
        w0 = p1 - p2
        a = np.dot(d1, d1)
        b = np.dot(d1, d2)
        c = np.dot(d2, d2)
        d = np.dot(d1, w0)
        e = np.dot(d2, w0)

        t1 = (b * e - c * d) / (a * c - b ** 2)

        intersection_point = p1 + t1 * d1
        return intersection_point

    else:
        # Lines are parallel and coincident, return None
        return None

def find_nearest_distance(p1, d1, p2, d2):
    w0 = p1 - p2
    a = np.dot(d1, d1)
    b = np.dot(d1, d2)
    c = np.dot(d2, d2)
    d = np.dot(d1, w0)
    e = np.dot(d2, w0)

    t1 = (b * e - c * d) / (a * c - b ** 2)
    t2 = (a * e - b * d) / (a * c - b ** 2)

    nearest_point_line1 = p1 + t1 * d1
    nearest_point_line2 = p2 + t2 * d2

    nearest_distance = np.linalg.norm(nearest_point_line1 - nearest_point_line2)
    return nearest_distance, nearest_point_line1, nearest_point_line2

def find_midpoint(p1, p2):
    return (p1 + p2) / 2