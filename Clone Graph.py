from collections import defaultdict, deque
from itertools import product
from termcolor import colored
import timeit

def validate(actual, target):
    if isinstance(target, list):
        if len(actual) != len(target):
            return False
        for a, t in zip(actual, target):
            if not validate(a, t):
                return False
        return True
    else:
        return actual == target

def test_output(actual, target):
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    if validate(actual, target):
        print(colored("Passed!", "green"))
        return True
    else:
        print(colored("Failed", "red"))
        return False

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(adjList):
    if len(adjList) == 0:
        return None
    graph = {}

    for i in range(1, len(adjList)+1):
        graph[i] = Node(i)
        
    for i, edge in enumerate(adjList):
        for e in edge:
            graph[i+1].neighbors.append(graph[e])
    
    return graph[1]

def graph2list(node):
    res = []
    if not node:
        return res
    seen = set()
    seen.add(node.val)
    stack = []
    stack.append(node)
    while len(stack) > 0:
        cur_node = stack.pop()
        tmp = []
        for n in cur_node.neighbors:
            tmp.append(n.val)
            if n.val not in seen:
                stack.append(n)
                seen.add(n.val)
        res.append(tmp)
    return res

class Solution: 
    # def cloneGraph(self, node):
    #     if not node:
    #         return None
        
    #     seen = set()
    #     new_nodes = dict()
        
    #     def dfs(cur_node):
    #         if cur_node.val in seen:
    #             return
            
    #         seen.add(cur_node.val)
    #         new_nodes[cur_node] = Node(cur_node.val)
            
    #         for n in cur_node.neighbors:
    #             dfs(n)
        
    #     dfs(node)
    #     for origin_node, new_node in new_nodes.items():
    #         for n in origin_node.neighbors:
    #             new_node.neighbors.append(new_nodes[n])
        
    #     return new_nodes[node]

    def cloneGraph(self, node):
        if not node:
            return None
        
        seen = set()
        new_nodes = dict()
        stack = []
        stack.append(node)        
        while len(stack) > 0:
            cur_node = stack.pop()
            if cur_node.val in seen:
                continue
            
            seen.add(cur_node.val)
            new_nodes[cur_node] = Node(cur_node.val)
            
            for n in cur_node.neighbors:
                stack.append(n)
        
        for origin_node, new_node in new_nodes.items():
            for n in origin_node.neighbors:
                new_node.neighbors.append(new_nodes[n])
        
        return new_nodes[node]



    # def cloneGraph(self, node):
    #     if not node:
    #         return None
    #     new_nodes = {}
    #     new_edges = set()
    #     stack = deque()
    #     stack.append(node)
        
    #     while len(stack) > 0:
    #         cur_node = stack.popleft()
    #         cur_val = cur_node.val

    #         if cur_val not in new_nodes:
    #             new_nodes[cur_val] = Node(cur_val)
            
    #         for n in cur_node.neighbors:
    #             nbrs_val = n.val
    #             if nbrs_val not in new_nodes:
    #                 new_nodes[nbrs_val] = Node(nbrs_val)
    #             if (cur_val, nbrs_val) not in new_edges:
    #                 new_edges.add((cur_val, nbrs_val))
    #                 new_nodes[cur_val].neighbors.append(new_nodes[nbrs_val])
                
    #             if (nbrs_val, cur_val) not in new_edges:
    #                 stack.append(n)

    #     return new_nodes[1]

def main():
    sol = Solution()

    test_cases = [
                    ([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]),
                    # ([[2],[1]], [[2],[1]]),
                    # ([[]], [[]]),
                    # ([], []),
                    # ([[2],[1]], [[2],[1]])
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        node = buildGraph(input)
        
        start = timeit.default_timer()
        actual = sol.cloneGraph(node)
        stop = timeit.default_timer()

        actual = graph2list(actual)
        if not test_output(actual, target):
            all_passed = False
        print('Time: ', stop - start) 
    
    print()
    if all_passed:
        print(colored("All tests passed!", "green"))
    else:
        print(colored("Not all tests passed!", "red"))


if __name__ == '__main__':
    main()