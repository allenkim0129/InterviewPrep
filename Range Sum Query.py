from collections import defaultdict
from itertools import product
import timeit

def test_output(actual, target):
    print()
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 

class NumArray:

    def __init__(self, nums):
        self.pre_sum = [0]
        for num in nums:
            self.pre_sum.append(num + self.pre_sum[-1])
        
    def sumRange(self, left, right):
        return self.pre_sum[right+1] - self.pre_sum[left]

class Solution:
    def test(self, inputs, targets):
        commands = inputs[0]
        nums = inputs[1]

        numArray = None
        actual = []
        for command, num in zip(commands, nums):
            if command == 'NumArray':
                numArray = NumArray(num[0])
                actual.append(None)
            elif command == 'sumRange':
                actual.append(numArray.sumRange(num[0], num[1]))
            
        test_output(actual, targets)
        


def main():
    sol = Solution()

    test_cases = [
                    ((["NumArray", "sumRange", "sumRange", "sumRange"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]), [None, 1, -1, -3])
                  ]
    
    sol = Solution()
    
    for test in test_cases:
        sol.test(test[0], test[1])



if __name__ == '__main__':
    main()