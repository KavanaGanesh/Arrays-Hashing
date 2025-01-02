from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''find the index using total length // 2, return the index of that element after sorting list'''
        res = sorted(nums)[len(nums)//2]
        return res
            

                

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
nums = [2,4,4,4,4,4,2,2,2,2,2,2]


print(Solution().majorityElement(nums))