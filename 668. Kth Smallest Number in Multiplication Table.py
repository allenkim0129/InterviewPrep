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
    print()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    if validate(actual, target):
        print(colored("Passed!", "green"))
        return True
    else:
        print(colored("Failed", "red"))
        return False

class Solution: 
    def findKthNumber(self, m, n, k):
        lo = 0
        hi = m*n + 1

        while (lo < hi):
            mid = (lo + hi) // 2

            cnt = 0
            for i in range(1, m+1):
                cnt += min(n, mid//i)
            
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
            
        return lo

def main():
    sol = Solution()

    test_cases = [
                    # ((3,3,5), 3),
                    # ((2,3,6),6),
                    ((9895, 28405, 100787757), 31666344)
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.findKthNumber(*input)
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