from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[counter] = nums[i]
                counter+=1
        return counter + 1
            

nums = [1,2,2,3,3,4,5]
print(Solution().removeDuplicates(nums))