from collections import defaultdict
from itertools import product
from termcolor import colored
import timeit
import math

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
    def judgeSquareSum(self, c):
        b = int(math.sqrt(c))

        while b >= 0:
            a = math.sqrt(c-(b*b))
            if a == int(a):
                return True
            
            b -= 1
        
        return False

def main():
    sol = Solution()

    test_cases = [
                    # (5, True),
                    # (3, False),
                    # (4, True),
                    # (2, True),
                    # (1, True),
                    ((1<<31) - 1, False)                 
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.judgeSquareSum(input)
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