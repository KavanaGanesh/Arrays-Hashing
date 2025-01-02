from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] != val:
                nums[counter] == nums[i]
                counter+=1
        return counter


# case1:
# nums = [3,2,2,3]
# val = 3
# Output: 2, nums = [2,2,_,_]
# case2:
nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
print(Solution().removeElement(nums, val))