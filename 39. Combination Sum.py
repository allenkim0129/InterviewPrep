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
    def combinationSum(self, candidates, target):
        candidates.sort()
        
        def rec(cid, t):
            ans = []
            
            for i in range(cid, len(candidates)):
                if candidates[i] == t:
                    ans.append([candidates[i]])
                    break
                if candidates[i] > t:
                    break

                new_t = t - candidates[i]
                if candidates[i] <= new_t:
                    ret = rec(i, new_t)
                    
                    if len(ret) > 0:
                        for r in ret:
                            ans.append([candidates[i]] + r)
            
            return ans
        
        return rec(0, target)

def main():
    sol = Solution()

    test_cases = [
                    ([[2], 1], []),
                    ([[2,3,5], 8], [[2,2,2,2],[2,3,3],[3,5]]),
                    ([[2,3,6,7], 7], [[2,2,3],[7]]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.combinationSum(input[0], input[1])
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