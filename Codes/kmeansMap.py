"""mapper.py

__author__ = "aziz"
"""
import sys
from math import sqrt
import time


def computeDistance(x,y):
    return sqrt(sum([(a - b)**2 for a,b in zip(x,y)])**(0.5))

startTime = time.time()
for line in sys.stdin:
    line = line.strip()
    coor = [int(x) for x in line.split(',')]
    closestCentroid = 0;
    closestDist = computeDistance(coor,centroids[0]);
    for i in xrange(1,10):
        dist = computeDistance(coor,centroids[i])
        if dist<closestDist:
            closestCentroid = i
            closestDist = dist
    print(str(closestCentroid)+'\t'+line)
