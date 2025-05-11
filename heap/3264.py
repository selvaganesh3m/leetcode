#https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/

import heapq

nums = [2,1,3,5,6]
k = 5
multiplier = 2

heap = [(val, idx) for idx, val in enumerate(nums)]
heapq.heapify(heap)

for _ in range(k):
    val, idx = heapq.heappop(heap)
    print(val, idx)
    val *= multiplier
    nums[idx] = val
    heapq.heappush(heap, (val,idx))

print(nums)