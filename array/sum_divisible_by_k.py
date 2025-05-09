

# Question URL
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val = sum(nums)
        if val % k == 0:
            return 0
        if k > val:
           return val
        max_val = (val // k) * k
        return abs(max_val - val)
        
    


        
