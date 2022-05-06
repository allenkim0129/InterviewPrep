from collections import defaultdict
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

class Solution: 
    def islandPerimeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        perimeter = 0              

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    perimeter += 4

                    if r > 0 and grid[r-1][c]:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1]:
                        perimeter -= 2

        return perimeter

    # def islandPerimeter(self, grid):
    #     m = len(grid)
    #     n = len(grid[0])
    #     sum = 0
    #     for r in range(m):
    #         for c in range(n):
    #             if c > 0:
    #                 if grid[r][c] != grid[r][c-1]:
    #                     sum += 1
    #             else:
    #                 sum += grid[r][c]

    #             if r > 0:
    #                 if (grid[r][c] != grid[r-1][c]):
    #                     sum += 1
    #             else:
    #                 sum += grid[r][c]
    #         sum += grid[r][c]
        
    #     for c in range(n):
    #         sum += grid[r][c]

    #     return sum

    # #recursive
    # def islandPerimeter(self, grid):
    #     m = len(grid)
    #     n = len(grid[0])
    #     global visited
    #     visited = [[0]*n for _ in range(m)]

    #     def rec(r, c, grid):
    #         global visited
    #         if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
    #             return 1
            
    #         if visited[r][c]:
    #             return 0

    #         visited[r][c] = 1

    #         sum = 0
    #         for loc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
    #             sum += rec(*loc, grid)
            
    #         return sum

    #     for r in range(m):
    #         for c in range(n):
    #             if grid[r][c]:
    #                 return rec(r, c, grid)
        
    #     return 0
        
def main():
    sol = Solution()

    test_cases = [
                    ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16),
                    ([[1]], 4),
                    ([[1,0]], 4),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.islandPerimeter(input)
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