class Solution(object):
    def maxprod(self, nums):

        if not nums:
            return 0
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            if current<0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(current, max_prod*current)
            min_prod = min(current, min_prod*current)
            result = max(result, max_prod)

        return result
