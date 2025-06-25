class Solution(object):
    def duplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False