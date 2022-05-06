from collections import defaultdict
from itertools import product
from termcolor import colored
import timeit
import bisect

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
    def fallingSquares(self, positions):
        pos = [0]
        height = [0]
        sol = []
        
        max_height = 0
        for i,j in positions:
            l = bisect.bisect_right(pos, i) # idx larger than i
            r = bisect.bisect_left(pos, i+j) # idx larger than or equal to i+j
            curr_height = j + max(height[l-1:r] or [0])
            pos[l:r] = [i,i+j]
            height[l:r] = [curr_height, height[r-1]]
            max_height = max(curr_height, max_height)
            sol.append(max_height)
        return sol

    # def fallingSquares(self, positions):
    #     #build graph
    #     graph = defaultdict(list)
    #     for i in range(len(positions)-1):
    #         lo, hi = positions[i]
    #         hi += lo
    #         for j in range(i + 1, len(positions)):
    #             lo2, hi2 = positions[j]
    #             hi2 += lo2
                
    #             #check overlaps
    #             if (lo <= lo2 < hi
    #                 or lo2 <= lo < hi2):
    #                 graph[j].append(i)
        
    #     max_h = 0
    #     dp = [0]*len(positions)
    #     res = []
        
    #     for i in range(len(positions)):
    #         if i in graph:
    #             local_max = 0
    #             for j in graph[i]:
    #                 local_max = max(local_max, dp[j])
    #             dp[i] = local_max
    #         dp[i] += positions[i][1]
            
    #         if dp[i] > max_h:
    #             max_h = dp[i]
            
    #         res.append(max_h)
        
    #     return res

def main():
    sol = Solution()

    test_cases = [
                    ([[1,2],[2,3],[6,1]], [2,5,5]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.fallingSquares(input)
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