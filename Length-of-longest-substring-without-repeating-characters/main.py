class Solution(object):
    def max_length(self, s):

        char_set = set()
        left = 0
        max_sum = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])
            max_length = max(max_length, right-left+1)

        return max_length