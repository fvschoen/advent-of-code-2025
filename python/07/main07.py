from typing import List
import functools

def part01_count_splits(manifold: List[List[str]]) -> int:
    
    n, m, j = len(manifold), len(manifold[0]), 0
    while manifold[0][j] != 'S':
        j += 1

    visited = set([])
    def dfs(i: int, j: int) -> int:

        if i >= n - 1 or j < 0 or j > m - 1: return 0 
        if (i, j) in visited: return 0
        visited.add((i, j))

        if manifold[i + 1][j] == '^':
            return 1 + dfs(i + 1, j -1) + dfs(i + 1, j + 1)
        return dfs(i + 1, j)

    return dfs(0, j)

def part02_count_splits(manifold: List[List[str]]) -> int:
    
    n, m, j = len(manifold), len(manifold[0]), 0
    while manifold[0][j] != 'S':
        j += 1

    @functools.cache
    def dp(i: int, j: int) -> int:

        if i >= n - 1 or j < 0 or j > m - 1: return 0 

        if manifold[i + 1][j] == '^':
            splits = 1
            splits += dp(i + 1, j - 1)
            splits += dp(i + 1, j + 1)
            return splits
        return dp(i + 1, j)

    return dp(0, j) + 1

if __name__ == "__main__":

    with open("input07.txt", "r") as f:
        manifold = f.readlines()
        manifold = [list(line.strip()) for line in manifold]

    print ("""--- Part One ---""")
    print ("Number of splits: {0}".format(part01_count_splits(manifold)), "\n")

    print ("""--- Part Two ---""")
    print ("Number of splits: {0}".format(part02_count_splits(manifold)), "\n")
