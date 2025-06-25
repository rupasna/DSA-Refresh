class Solution(object):
    def intersect(self, nums1, nums2):
        from collections import Counter

        count_map = Counter(nums1)
        result = []

        for num in nums2:
            if count_map[num]>0:
                result.append(num)
                count_map[num]-=1
        return result

