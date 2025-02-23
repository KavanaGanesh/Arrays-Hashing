from typing import List
from collections import Counter

# 1) Pass the list into counter method, the result will be the key: value (key(is the number), value is the frequency)
# 2) need to print the max value: syntax : max(counter, key = counter.get)
# Complexities: Space: creating a counter = O(n), Time = passing the list and creaying the frequency = O(n) 

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         '''find the index using total length // 2, return the index of that element after sorting list'''
#         res = sorted(nums)[len(nums)//2]
#         return res
            
class Solution:
    def majorityElement(self, nums):
        nums_count = Counter(nums)
        return max(nums_count, key =nums_count.get )
        # return [word for word, count in nums_count.most_common(1)] # this is if you want to print in the list format
        # use counter.most_common() ""
                

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
nums = [2,4,4,4,4,4,2,2,2,2,2,2]


print(Solution().majorityElement(nums))