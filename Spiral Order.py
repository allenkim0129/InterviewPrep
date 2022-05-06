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
    def spiralOrder(self, matrix):
        
        def rec(matrix, r, c, dr, dc, r_min, r_max, c_min, c_max):
            res = []
            if dc > 0:
                if c < c_max:
                    res = matrix[r][c: c_max]
                    r += 1
                    c_max -= 1
                    c = c_max
                    dr = 1
                    dc = 0
                    
            elif dr > 0:
                if r < r_max:
                    res = [matrix[i][c] for i in range(r, r_max)]
                    r_max -= 1
                    r = r_max
                    c -= 1                   
                    dr = 0
                    dc = -1
                    
            elif dc < 0:
                if c > c_min:
                    c_min += 1
                    res = [matrix[r][i] for i in reversed(range(c_min, c+1))]
                    r -= 1
                    c = c_min
                    dr = -1
                    dc = 0
            elif dr < 0:
                if r > r_min:
                    r_min += 1
                    res = [matrix[i][c] for i in reversed(range(r_min, r+1))]
                    r = r_min
                    c += 1
                    dr = 0
                    dc = 1
            
            if len(res) > 0:
                return res + rec(matrix, r, c, dr, dc, r_min, r_max, c_min, c_max)
            else:
                return []
        
        return rec(matrix, 0, 0, 0, 1, 0, len(matrix), -1, len(matrix[0]))

def main():
    sol = Solution()

    test_cases = [
                    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], []),
                    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.spiralOrder(input)
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