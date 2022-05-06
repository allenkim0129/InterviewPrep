from collections import defaultdict
from itertools import product
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
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))

    assert(validate(actual, target))

class Solution: 
    def findSubstring(self, s, words):
        wlen = len(words[0])
        n = len(words)
        subs_len = wlen * n
        
        # words = set(words)
        words_counts = defaultdict(int)
        for word in words:
            words_counts[word] += 1

        res = []        
        for i in range(len(s) - subs_len + 1):
            sub_str_start = i
            sub_str_end = i + subs_len
            seen = defaultdict(int)
            found = True
            while sub_str_start < sub_str_end:
                sub_str = str(s[sub_str_start:sub_str_start+wlen])
                if (sub_str not in words_counts
                    or (sub_str in seen 
                        and seen[sub_str] == words_counts[sub_str])):
                    found = False
                    break
                
                seen[sub_str] += 1
                sub_str_start += wlen
            
            if found:
                res.append(i)

        return res

def main():
    sol = Solution()

    test_cases = [
                    (("barfoothefoobarman", ["foo","bar"]), [0,9]),
                    (("wordgoodgoodgoodbestword", ["word","good","best","word"]), []),
                    (("barfoofoobarthefoobarman", ["bar","foo","the"]), [6,9,12]),
                    (("bardfoobardfoob", ["foob","bard"]), [0,7]),
                    (("wordgoodgoodgoodbestword", ["word","good","best","good"]), [8])
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.findSubstring(*input)

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()