import itertools
import math
from typing import List, Dict, Tuple
import heapq
import functools
import operator

class UnionFind:
    def __init__(self, n_size):
        self.n = n_size
        self.parent = list(range(n_size))
        self.size = [1] * n_size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
 
        if x_root == y_root:
            return

        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.n -= 1
        return
    
    def cluster_size(self, x):
        return self.size[self.find(x)]

def dist(x: List[int], y: List[int]) -> float:
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)

def calc_pairs_distance(points: Dict[int, List[int, int, int]]) -> Tuple[Tuple[int, int], float]:
    pairwise = itertools.combinations(points.keys(), 2)
    pairwise_distances = [(dist(points[x], points[y]), (x, y)) for x, y in pairwise]
    pairwise_distances = sorted(pairwise_distances, reverse=False, key=lambda x: x[0])
    return pairwise_distances

def part01_union_find_pairs(points: Dict[int, List[int, int, int]], pairwise_distances: List[Tuple[float, Tuple[int, int]]], max_connections: int = 1000) -> List[Tuple[float, Tuple[int, int]]]:
    n = len(points)
    union_find = UnionFind(n)
    
    for (dist, (i, j)) in pairwise_distances[:max_connections]:
        union_find.union(i, j)

    roots = {union_find.find(i) for i in union_find.parent}
    sizes = sorted([union_find.size[r] for r in roots], reverse=True)
    return functools.reduce(operator.mul, sizes[:3])
    
def part02_union_find_pairs(points: Dict[int, List[int, int, int]], pairwise_distances: List[Tuple[float, Tuple[int, int]]]) -> List[Tuple[float, Tuple[int, int]]]:
    n = len(points)
    union_find = UnionFind(n)
    
    for (dist, (i, j)) in pairwise_distances:
        union_find.union(i, j)
        if union_find.n == 1:
            break

    return points[i][0] * points[j][0]

if __name__ == "__main__":

    with open("input08.txt", 'r') as f:
        points = f.readlines()
        points = [[int(coord) for coord in line.strip().split(',')] for line in points]
        points = dict(zip(range(len(points)), points))
        pairwise_distances = calc_pairs_distance(points)

    print ("--- Part One ---")
    print ("Product size three largest: {0}".format(part01_union_find_pairs(points, pairwise_distances, max_connections=1000)), "\n")

    print ("""--- Part Two ---""")
    print ("Product x-coord of last two: {0}".format(part02_union_find_pairs(points, pairwise_distances)), "\n")