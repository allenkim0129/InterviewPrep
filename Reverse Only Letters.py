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
    def reverseOnlyLetters(self, s):
        l = 0
        r = len(s)-1
        cs = list(s)
        while l < r:
            if not cs[l].isalpha():
                l += 1
            elif not cs[r].isalpha():
                r -= 1
            else:
                cs[l], cs[r] = cs[r], cs[l]
                
                l += 1
                r -= 1
        
        return ''.join(cs)

def main():
    sol = Solution()

    test_cases = [
                    ("7_28]", "7_28]"),
                    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.reverseOnlyLetters(input)
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