import sys
import itertools
from typing import List, Tuple, TextIO
import functools
import operator

def parse_math(ops: List[str]) -> List[str]:
    return [list(map(int, line.split()))  if not '+' in line else line.split() for line in ops]

def part01_sum_problems(ops: List[Tuple[int], Tuple[int], Tuple[int], Tuple[str]]) -> int:
    w, x, y, z, op = ops[0], ops[1], ops[2], ops[3], ops[4]
    op_map = {'+': operator.add, '*': operator.mul}

    return sum(list(map(lambda x : functools.reduce(x[-1], x[0]), \
                        (list(zip(zip(w, x, y, z), map(lambda x : op_map[x], op)))))))

def a_new_parse(f: TextIO) -> List[str]:
    
    preprocessed_problems = "\n".join(["".join(zipline) for zipline in itertools.zip_longest(*[line.rstrip() for line in f], fillvalue='')])
    op_map = {'+': operator.add, '*': operator.mul}

    def proc_line(line: str):
        if line.strip() == "": return None
        elif line[-1] in ['+', '*']:
            found_op = line[-1]
            val = int(line[:-1].strip())
            yield op_map[found_op]
            yield val
        else:
            val = int(line.strip())
            yield val
        
    column = [list(proc_line(line)) if line != '' else 0 for line in preprocessed_problems.split('\n')]
    column = [item for sublist in column for item in sublist]

    return column

    
def part02_sum_problems(column: List[int]) -> int:

    problems = []
    curr_op = None
    curr_operands = []

    for item in column:
        if callable(item):
            if curr_op:
                problems.append((curr_op, curr_operands))
            curr_op = item
            curr_operands = []
        else:
            curr_operands.append(item)
    if curr_op: problems.append((curr_op, curr_operands))

    run_sum = sum(list(map(lambda x : functools.reduce(x[0], x[1]), problems)))

    return run_sum
    

if __name__ == "__main__":

    with open("input06.txt", 'r') as f:
        raw = f.readlines()

    ops = parse_math(raw)

    print ("""--- Part One ---""")
    print ("Sum of problems: {0}".format(part01_sum_problems(ops)), "\n")

    with open("input06.txt", 'r') as f:
            raw_tp = a_new_parse(f)
            
    print ("""--- Part Two ---""")
    print ("Sum of problems: {0}".format(part02_sum_problems(raw_tp)), "\n")