#!/usr/bin/env python3
import csv
import time
from itertools import permutations

def check_graph(nodes, adjacency_list):
    # generate all possible paths to visit every node once
    possible_paths = permutations(nodes)

    # check if any path is valid
    for path in possible_paths:
        valid_path = True 
        if len(path) == 1:  # if only one node
            return True
        for i in range(len(path) - 1):
            # check if the edge exists between consecutive nodes
            if path[i+1] not in adjacency_list.get(path[i], []):
                valid_path = False  # no edge found
                break
        if valid_path:
            return True  # found a path
    return False  # no valid path found

def generate_graphs():
    file_name = "./testing_graphs_tfriedma.cnf"
    # file_name = "./timing_graphs_tfriedma.cnf"
    with open(file_name, mode ='r') as file:
        csvFile = csv.reader(file)
        csvList = list(csvFile) # convert to list so .pop() can be used
        case = 0 # to keep track of which graph we are on
        directed = False # to indicate directed/undirected graph
        while(csvList):
            line = csvList.pop(0)
            if (line[0] == 'c'): # new graph start
                case += 1
                line = csvList.pop(0)
                if line[1] == ' u': # update directed if u
                    directed = False
                else:
                    directed = True
                nNodes = int(line[2][1:]) # number of nodes
                nEdges = int(line[3][1:]) # number of edges
                line = csvList.pop(0)
                nodes = [int(v[1:]) for v in line[1:]] # get the node names
                adjacency_list = {} # initial adjacency list
                for _ in range(nEdges): # get all of the edges
                    line = csvList.pop(0)
                    n1 = int(line[1][1:])
                    n2 = int(line[2][1:])
                    if n1 in adjacency_list.keys(): # add to adjacency list
                        adjacency_list[n1].add(n2)
                    else:
                        adjacency_list[n1] = set([n2])
                    if not directed: # add opposite directed node if graph is not directed
                        if n2 in adjacency_list.keys():
                            adjacency_list[n2].add(n1)
                        else:
                            adjacency_list[n2] = set([n1])
                yield (nodes, adjacency_list, case) # yield the graph

def test_graphs():
    graphs = generate_graphs() # get the graphs to test
    pretty_print = True # set this to false if you want results printed to terminal in csv format
    for nodes, adjacency_list, case in graphs:
        start_time = time.time() # start timer
        check = check_graph(nodes, adjacency_list) # check graph
        end_time = time.time() # end timer 
        elapsed_time = end_time - start_time # get time
        # print results
        if pretty_print:
            if check:
                print(f"Case {case:2.0f}, {len(nodes):2.0f} nodes: Found solution.    Elapsed time: {elapsed_time:0.4f} seconds")
            else:
                print(f"Case {case:2.0f}, {len(nodes):2.0f} nodes: No Solution Found. Elapsed time: {elapsed_time:0.4f} seconds")
        else:
            if check:
                print(f"{case}, {len(nodes)}, {elapsed_time:0.8f}, 1")
            else:
                print(f"{case}, {len(nodes)}, {elapsed_time:0.8f}, 0")

# run the solution
test_graphs()