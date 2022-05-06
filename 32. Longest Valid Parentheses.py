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
    #stack solution
    def longestValidParentheses(self, s):
        stack = [-1]
        cur_len = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: 
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    cur_len = i - stack[-1]
                    max_len = max(max_len,cur_len)
                    
        return max_len

    # def longestValidParentheses(self, s):
    #     l_cnt = 0
    #     r_cnt = 0
    #     max_len = 0
    #     for c in s:
    #         if c == '(':
    #             l_cnt += 1
    #         else:
    #             r_cnt += 1
            
    #         if l_cnt == r_cnt:
    #             if l_cnt > max_len:
    #                 max_len = l_cnt
    #         elif r_cnt > l_cnt:
    #             l_cnt = r_cnt = 0
        
    #     l_cnt = 0
    #     r_cnt = 0
    #     for c in reversed(s):
    #         if c == '(':
    #             l_cnt += 1
    #         else:
    #             r_cnt += 1
            
    #         if l_cnt == r_cnt:
    #             if l_cnt > max_len:
    #                 max_len = l_cnt
    #         elif r_cnt < l_cnt:
    #             l_cnt = r_cnt = 0
        
    #     return max_len * 2

def main():
    sol = Solution()

    test_cases = [
                    ("()(()", 2),
                    ("(()", 2),
                    (")()())", 4),
                    ("", 0),
                    ("(((((((((()(()", 2),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.longestValidParentheses(input)
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