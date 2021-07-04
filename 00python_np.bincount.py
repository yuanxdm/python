import numpy as np

x1 = np.array([2,3,1,2,1,3,4,2,1,4])
print(np.bincount(x1))

x2 = np.array([1, 1, 3, 2, 1, 7])
print(np.bincount(x2))

"""表示从0到最大数，每个数的个数，没有数的是0"""