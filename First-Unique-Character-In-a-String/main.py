from collections import Counter

class Solution(object):
    def unique(self, s):
        count_char = Counter(s)

        for i in range(len(s)):
            if count_char[s[i]]==1:
                return i
        
        return -1
