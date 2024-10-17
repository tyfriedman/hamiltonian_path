#!/usr/bin/env python3
import csv
import time
from itertools import permutations

def check_graph(nodes, adjacency_list):
    # generate all possible paths to visit every node once
    possible_paths = permutations(nodes)
    # print(adjacency_list)
    # if len(adjacency_list.keys()) < len(nodes) - 1:
    #     return False

    # check if any path is valid
    for path in possible_paths:
        valid_path = True 
        if len(path) == 1:  # if only one node
            return True
        for i in range(len(path) - 1):
            # check if the edge exists between consecutive nodes
            if path[i+1] not in adjacency_list.get(path[i], []):
                valid_path = False  # no edge - invalid
                break
        if valid_path:
            # print(path)
            return True  # found a path
    return False  # no valid path found


def generate_graphs():
    file_name = "./hamiltonian_path_test_cases2.cnf"
    with open(file_name, mode ='r') as file:
        csvFile = csv.reader(file)
        csvList = list(csvFile) # convert to list so .pop() can be used
        case = 0 # to keep track of which graph we are on
        directed = False # to indicate directed/undirected graph
        while(csvList):
            line = csvList.pop(0)
            if (line[0] == 'c'):
                case += 1
                line = csvList.pop(0)
                if line[1] == ' u':
                    directed = False
                else:
                    directed = True
                nNodes = int(line[2][1:])
                nEdges = int(line[3][1:])
                line = csvList.pop(0)
                nodes = [int(v[1:]) for v in line[1:]]
                adjacency_list = {}
                for _ in range(nEdges):
                    line = csvList.pop(0)
                    n1 = int(line[1][1:])
                    n2 = int(line[2][1:])
                    if n1 in adjacency_list.keys():
                        adjacency_list[n1].add(n2)
                    else:
                        adjacency_list[n1] = set([n2])
                    if not directed:
                        if n2 in adjacency_list.keys():
                            adjacency_list[n2].add(n1)
                        else:
                            adjacency_list[n2] = set([n1])
                yield (nodes, adjacency_list, case)


def test_graphs():
    graphs = generate_graphs()
    for nodes, adjacency_list, case in graphs:
        start_time = time.time()
        if (check_graph(nodes, adjacency_list)):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Found solution for case {case} with {len(nodes)} nodes in {elapsed_time:0.4f} seconds.")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"No solution found for case {case} with {len(nodes)} nodes. Took {elapsed_time:0.4f} seconds.")

test_graphs()