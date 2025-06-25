class Solution(object):
    def lcp(self,s):
        if not s:
            return ""
        
        prefix = s[0]

        for word in s[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
                
        return prefix