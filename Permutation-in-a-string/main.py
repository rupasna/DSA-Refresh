class Solution(object):
    def permutation(self, s1, s2):

        from collections import Counter

        len1 = len(s1)
        len2 = len(s2)

        if len1>len2:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        if s1_count == window_count:
            return True
        
        for i in range(len1, len2):

            start_char = s2[i-len1]
            end_char = s2[i]

            window_count[start_char]-=1
            window_count[end_char]+=1

            if window_count[start_char]==0:
                del window_count[start_char]

            if window_count == s1_count:
                return True
            
        return False