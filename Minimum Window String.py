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

class Solution:
    # def test(self, s, t):
    #     char_counts = {}
    #     total_counts = 0
    #     for c in t:
    #         if c in char_counts:
    #             char_counts[c] += 1
    #         else:
    #             char_counts[c] = 1
    #         total_counts += 1
        
    #     min_start = 0
    #     min_end = -1
    #     min_len = int(10e5)
    #     stack = []
    #     for i, c in enumerate(s):
    #         if c in char_counts:
    #             if char_counts[c] > 0:
    #                 char_counts[c] -= 1
    #                 total_counts -= 1
    #             else:
    #                 for sid, value in enumerate(stack):
    #                     if value[0] == c:
    #                         stack.pop(sid)
    #                         break
    #             stack.append((c, i))

    #             if total_counts == 0:
    #                 cur_len = stack[-1][1] - stack[0][1]

    #                 if cur_len < min_len:
    #                     min_len = cur_len
    #                     min_start = stack[0][1]
    #                     min_end = stack[-1][1]
        
    #     return str(s[min_start:min_end+1])  

    def test(self, s, t):
        char_counts = defaultdict(int)
        total_counts = len(t)
        for c in t:
            char_counts[c] += 1

        min_start = 0
        min_end = len(s) - 1
        start = 0
        for end, c in enumerate(s):
            if c in char_counts:
                if total_counts > 0 and char_counts[c] > 0:
                    total_counts -= 1
                
                char_counts[c] -= 1
                
                if total_counts == 0:
                    while start < len(s):
                        if s[start] in char_counts:
                            if char_counts[s[start]] < 0:
                                char_counts[s[start]] += 1
                            else:
                                break
                        start += 1

                    if end - start < min_end - min_start:
                        min_start, min_end = start, end
        
        if total_counts == 0:
            return str(s[min_start:min_end+1])
        else:
            return ""


def main():
    sol = Solution()

    test_cases = [
                    (("bba", "ab"), "ba"),
                    # (("ABBBBBBBBBBBBBBBBBBBBBBBBBBBCDEFGHIJKLMNOPQRSTUVWXYZBBY", "BBY"), "BBY")
                    # (("ADOBECODEBANC", "ABC"), "BANC"),
                    # (("a", "a"), "a"),
                    # (("a", "aa"), ""),
                    # (("AAFTBCABC", "ABC"), "BCA")
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.test(input[0], input[1])

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()