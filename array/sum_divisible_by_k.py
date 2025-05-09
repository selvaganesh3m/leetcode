

#https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val = sum(nums)
        operation = 0
        max_val = 0
    
        if val % k == 0:
            return 0

        if k > val:
            for i in nums:
                operation  += i - 0
            return operation

        for i in range(0, val + 1, k):
            max_val = i
        return abs(max_val - val)
        
