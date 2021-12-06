import heapq as hp
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    def _app1():
        hp.heapify(nums)
        for _ in range(len(nums)-k):
            hp.heappop(nums)
        return nums[0]

    def _app2():
        nums.sort()
        return nums[-k]

    return _app1()