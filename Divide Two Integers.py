from collections import defaultdict
from itertools import product
import timeit
import sys

def test_output(actual, target):
    print()
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 

class Solution: 
    def divide(self, dividend, divisor):
        if (dividend == -2147483648
            and divisor == -1):
            return 2147483647

        if (divisor == 1):
            return dividend

        res = 0
        a = abs(dividend)
        b = abs(divisor)
        pos = (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0)

        while a >= b:
            cnt = 0
            while a >= (b << (cnt + 1)):
                cnt += 1
            
            a -= b << cnt
            res += (1 << cnt)      

        return res if pos else -res

def main():
    sol = Solution()

    test_cases = [
                    ((10, 3), 3),
                    ((7,-3), -2),
                    ((0,1),0),
                    ((1,1),1),
                    ((-1,-1),1),
                    ((12, 3), 4),
                    ((-2147483648, 1), -2147483648),
                    ((-2147483648, -1), 2147483647),
                    ((2147483647, 1), 2147483647),

                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.divide(*input)

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()