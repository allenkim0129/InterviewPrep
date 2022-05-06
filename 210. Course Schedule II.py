from collections import defaultdict
from itertools import product
from typing import List
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

class Solution: 
    def findOrder(self, numCourses, prerequisites):
        result = []
        graph = defaultdict(list)

        #build graph
        for req in prerequisites:
            graph[req[0]].append(req[1])
        
        def DFS(id, seen):
            if id in seen:
                return

            seen.add(id)
            if id in graph:
                for j in graph[id]:
                    DFS(j, seen)

            result.append(id)
        
        seen = set()
        for i in range(numCourses):
            DFS(i, seen)
        return result

def main():
    sol = Solution()

    test_cases = [
                    ([2, [[1, 0]]], [0,1]),
                    ([4, [[1, 0],[2,0],[3,1],[3,2]]], [0,2,1,3]),
                    
                    ([4, [[3, 0],[1,0],[3,2],[2,1]] ], [0,3,2,1]),
                    ([4, [[1, 0],[3,0],[1,2],[2,3]] ], [0,1,2,3]),
                    # ([2, [[1, 0]]], [0,1]),
                    # ([2, [[1, 0]]], [0,1]),
                    # ([2, [[1, 0]]], [0,1]),
                    
                    #invalid
                    ([4, [[1,0],[2,0],[2,1],[1,3],[3,2]] ], []),
                    ([4, [[1,0],[3,0],[1,2],[2,3],[0,3]] ], []),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.findOrder(*input)
        stop = timeit.default_timer()

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