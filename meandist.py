# Python 3.10
# Calculate the mean distance between an array of points and the origin

import numpy as np
def mean_distance(points):
    return np.mean(np.linalg.norm(points, axis=1))
points = np.array([[1, 2, 3], [4, 5, 6]])
print(mean_distance(points))