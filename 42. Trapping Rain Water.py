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
    #left / right pointers
    def trap(self, height):
        l = 0
        r = len(height)-1
        l_max = 0
        r_max = 0

        area = 0
        while l < r:
            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]
            
            if l_max <= r_max:
                area += l_max - height[l]
                l += 1
            else:
                area += r_max - height[r]
                r -= 1
        
        return area

            

    #Stack
    # def trap(self, height):
    #     stack = []
    #     total_area = 0
    #     base = 0
    #     for i, h in enumerate(height):
    #         if not stack:
    #             stack.append((h,i))
    #             continue
            
    #         if h > stack[-1][0]:
    #             base, _ = stack.pop()
                
    #             #get all area when top of stack is less then h
    #             if stack:
    #                 while h >= stack[-1][0]:
    #                     top_h, top_i = stack.pop()
    #                     area_h = top_h - base
    #                     area_l = i - top_i -1
    #                     total_area += area_h * area_l

    #                     base = top_h
    #                     if not stack:
    #                         break
                
    #             #get all area where the top of the stack is greather than h
    #             if stack and base != h:
    #                 if h < stack[-1][0]:
    #                     area_h = h - base
    #                     area_l = i - stack[-1][1] -1
    #                     total_area += area_h * area_l

    #         stack.append((h,i))
    #         base = h
        
    #     return total_area


def main():
    sol = Solution()

    test_cases = [
                    ([4,2,0,3,2,5], 9),
                    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
                    ([2,1,2,6,9,7,5,5,7], 5),
                    ([2,0,2],2),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.trap(input)
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