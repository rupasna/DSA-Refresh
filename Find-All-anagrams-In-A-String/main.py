from collections import Counter

class Solution(object):
    def anagrams(self, s, p):

        p_count = Counter(p)
        window_count = Counter()
        result = []

        for i in range(len(s)):

            window_count[s[i]]+=1

            if i>=len(p):
                if window_count[s[i - len(p)]]==1:
                    del s[i-len(p)]

                else:
                    window_count[s[i-len(p)]]-=1

            if window_count == p_count:
                result.append(i - len(p)+1)
        return result


        