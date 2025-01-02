from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        new_dict = {}
        for idx, element in enumerate(nums):
            if element in new_dict.keys() and abs(new_dict[element]-idx)<=k:
                return True
            new_dict[element] = idx
        return False
    
# nums = [99,99]
# k=2
# nums = [1]
# k=1
# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))