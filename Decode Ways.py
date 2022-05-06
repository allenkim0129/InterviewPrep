from collections import defaultdict
from itertools import product
import timeit

##################################################################################################
# Decode Ways
# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.
##################################################################################################

def test_output(actual, target):
    print()
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 

class Solution: 
    def numDecodings(self, s):
        
        def rec(i):
            # pre-caluclated
            if i in counts:
                return counts[i]
            
            counts[i] = -1
            # out of bound
            if i >= len(s):
                counts[i] = 1
            elif s[i] == '0':
                counts[i] = 0
            #check if it can be mapped with second digit
            elif i + 1 < len(s):
                if s[i] == '1' or s[i] == '2':
                    if s[i+1] == '0':
                        counts[i] = rec(i+2)
                    elif (s[i] == '1'
                          or (s[i] == '2' and int(s[i+1]) < 7)):
                        counts[i] = rec(i+1) + rec(i+2)
            
            if counts[i] < 0:
                counts[i] = rec(i+1)
            
            return counts[i]            

        counts = {}
        return rec(0)

def main():
    sol = Solution()

    test_cases = [
                    ("10", 1),
                    ("10000", 0),
                    ("12", 2),
                    ("226", 3),
                    ("0", 0),
                    ("06", 0),
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        
        start = timeit.default_timer()
        actual = sol.numDecodings(input)

        test_output(actual, target)
        print(input)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()