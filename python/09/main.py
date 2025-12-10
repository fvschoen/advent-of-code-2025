from typing import List, Tuple

def rect_area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (1 + abs((x1 - x2))) * (1 + abs((y1 - y2)))

def part01_max_area(tiles: List[Tuple[int]]) -> Tuple[int, List[Tuple[Tuple[int, int], Tuple[int, int]]]]:
    n = len(tiles)
    max_area = 0
    rectangles = []
    for i in range(n):
        for j in range(i + 1, n):
            area = rect_area(tiles[i][0], tiles[i][1], tiles[j][0], tiles[j][1])
            max_area = max(max_area, area)
            rectangles.append((tiles[i], tiles[j]))
    return max_area, rectangles


def part02_overlap(rects: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:

    def area(P1: Tuple[int], P2: Tuple[int]) -> int:
        return (1 + abs(P1[0] - P2[0])) * (1 + abs(P1[1] - P2[1])) 


    rects = [(area(rect[0], rect[1]), rect) for rect in rects]
    rects.sort(reverse=True)
    # TODO


if __name__ == "__main__":

    with open('input09.txt', 'r') as f:
        gridtiles = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

    print ("""Part One""")
    max_area, rectangles = part01_max_area(gridtiles)
    print ("Max area:", max_area)

    print ("""Part Two""")
    overlap = part02_overlap(rectangles)
    print ("Overlap:", overlap)