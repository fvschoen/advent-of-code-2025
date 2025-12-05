from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def parse_ingredients(ingredients: List[str]) -> Tuple[List[List[int]], List[int]]:

    split_idx = ingredients.index('')
    raw_ranges = ingredients[:split_idx]
    ingredients = list(map(int, ingredients[split_idx + 1:]))

    ranges = []
    for r in raw_ranges:
        start, end = r.split('-')
        ranges.append([int(start), int(end)])

    ranges = merge_intervals(ranges)
    return (ranges, ingredients)

def part01_count_fresh_ingredients(ranges: List[List[int]], ingredients: List[int]) -> int:

    count = 0
    for ing in ingredients:
        for r_lower, r_upper in ranges:
            if r_lower <= ing <= r_upper:
                count += 1
                break

    return count

def part02_count_fresh_ingredients(ranges: List[List[int]]) -> int:

    count = 0
    for r_lower, r_upper in ranges:
        count += r_upper - r_lower + 1

    return count

if __name__ == "__main__":

    with open('input05.txt', 'r') as f:
        ingredients = [line.strip() for line in f]

    ranges, ingredients = parse_ingredients(ingredients)

    print ("""--- Part One ---""")
    print ("Number of fresh ingredients: {0}".format(part01_count_fresh_ingredients(ranges, ingredients)), "\n")

    print ("""--- Part Two ---""")
    print ("Number of fresh ingredients: {0}".format(part02_count_fresh_ingredients(ranges)), "\n")