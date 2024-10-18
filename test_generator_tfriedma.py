#!/usr/bin/env python3

import random
import math

def generate_test_case(n, case_num, has_solution):
    case_str = f"c, {case_num}, {'h' if has_solution else 'n'}\n"
    nodes = [node for node in range(n)]
    edges = set()
    if has_solution:
        num_edges = random.randint(n-1, n*(n-1))
        random.shuffle(nodes)
        for i in range(len(nodes) - 1):
            edges.add((nodes[i], nodes[i+1]))
    else:
        num_edges = random.randint(n-1, (n-2)*(n-1))
        random.shuffle(nodes)
        nodes.pop(0)

    for _ in range(num_edges - len(edges)):
        n1 = random.choice(nodes)
        n2 = random.choice(nodes)
        while n2 == n1:
            n2 = random.choice(nodes)
        if (n1, n2) not in edges and (n2, n1) not in edges:
            edges.add((n1, n2))

    case_str += f"p, u, {n}, {len(edges)}\n"
    node_str = ', '.join([str(node) for node in range(n)])
    case_str += f"v, {node_str}\n"
    for u, v in edges:
        case_str += f"e, {u}, {v}\n"
        
    return case_str


def generate_test_cases():
    case_num = 1
    test_cases = ""
    
    for n in range(3, 13): # this is the sizes of graphs that are to be tested
        for i in range(15): # number of graphs that have a solution
            test_cases += generate_test_case(n, case_num, True)
            case_num += 1
        for i in range(3): # number of graphs that have no solution
            test_cases += generate_test_case(n, case_num, False)
            case_num += 1
            
    return test_cases

# write the test cases to a file
with open('timing_graphs_tfriedma.cnf', 'w') as f:
    f.write(generate_test_cases())