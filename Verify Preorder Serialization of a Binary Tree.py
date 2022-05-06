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
    def isValidSerialization(self, preorder):
        preorder = preorder.split(',')
        
        stack = []
        for val in preorder:            
            while (stack
                    and val == '#'
                    and stack[-1] == '#'):
                    stack.pop()
                    if not stack:
                        return False
                    stack.pop()
            stack.append(val)

        if len(stack) == 1:
            return stack[0] == '#'
        else:
            return False

def main():
    sol = Solution()

    test_cases = [
                    ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
                    ("1,#", False),
                    ("9,#,#,1", False),
                    ("1,2,3,4,#,#,#,#,#", True),
                    ("1,#,#,#,#", False)
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.isValidSerialization(input)
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