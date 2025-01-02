from typing import List
from collections import Counter
import heapq
# k=2 this signifies find the 2 most significant(majority) elements
# its a heap DSA exercise


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(count)
        heap_list = []

# use dict.items() if you want both keys and values
        for number, freq in count.items():
            heapq.heappush(heap_list,(freq, number))

            if len(heap_list)>k:
                heapq.heappop(heap_list)
        # print(heap_list)

        return [k[1] for k in heap_list]

nums = [1,2,3,2,1,2]
k = 2
print(Solution().topKFrequent(nums,k))