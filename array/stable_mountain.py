
#https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        return [val for val in range(1, len(height)) if height[val - 1] > threshold]
