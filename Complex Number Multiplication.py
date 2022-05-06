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
    def complexNumberMultiply(self, num1, num2):
        #parse
        #num1 = a + bi
        #num2 = c + di
        num1 = num1.split("+")
        a = int(num1[0])
        b = int(num1[1][:-1])
        num2 = num2.split("+")
        c = int(num2[0])
        d = int(num2[1][:-1])

        #calculate
        # res = ac - bd + (ad + bc)i
        return "{}+{}i".format((a * c) - (b * d), (a*d) + (b * c))

def main():
    sol = Solution()

    test_cases = [
                    (("1+1i", "1+1i"), "0+2i"),
                    (("1+-1i", "1+-1i"), "0+-2i"),
                  ]
    
    sol = Solution()
    all_passed = True
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.complexNumberMultiply(*input)

        if not test_output(actual, target):
            all_passed = False
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
    
    print()
    if all_passed:
        print(colored("All tests passed!", "green"))
    else:
        print(colored("Not all tests passed!", "red"))


if __name__ == '__main__':
    main()