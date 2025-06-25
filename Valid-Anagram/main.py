class Solution(object):
    def anagram(self, s , t):
        return sorted(s) == sorted(t)