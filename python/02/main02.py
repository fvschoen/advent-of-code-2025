from typing import List, Tuple
import math

def parse_product_ids(product_ids: List[str]) -> List[Tuple(str, str)]:
    return [tuple(rng.split('-')) for rng in product_ids]

def part01_invalid_id_sum(product_ids: List[str]) -> int:
    def count_invalid_ids(rng: Tuple[str, str]) -> int:
        L_min, L_max = math.ceil(len(rng[0])/2), math.floor(len(rng[1])/2)
        for L in range(L_min, L_max+1):
            M = 10**L + 1
            pref_lo, pref_hi = max(10**(L - 1), math.ceil(int(rng[0]) / M)), min(10**L - 1, math.floor(int(rng[1]) / M))
            if pref_lo <= pref_hi:
                for X in range(pref_lo, pref_hi + 1):
                    yield X * 10**L + X

    return sum(sum(count_invalid_ids(rng)) for rng in product_ids)


if __name__ == "__main__":

    with open('input02.txt', 'r') as f:
        product_ids = f.readline().split(',')
        product_ids = parse_product_ids(product_ids)
    
    print ("--- Part One ---")
    print("""Sum of invalid IDs: {0}""".format(part01_invalid_id_sum(product_ids)))