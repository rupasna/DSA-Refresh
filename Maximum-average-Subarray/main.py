class Solution(object):
    def max_subarray(self, nums, k):
        window_sum = sum(nums[0:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum+=nums[right]-nums[right-k]
            max_sum = max(max_sum, window_sum)

        return float(max_sum)/k