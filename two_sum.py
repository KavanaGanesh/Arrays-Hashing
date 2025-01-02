from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for index, value in enumerate(nums):
            # print(index, value)
            # a(each_value of nums) +b(compliment) = target
            '''idea is to find the compliment that is b and check if complement of b exits in dictionary'''
            b = target-value
            '''store key-value: a-index  in the new_dict'''
            if b in new_dict: #if complement exits in new_dict
                return [index,new_dict[b]]
                # return new_dict
            new_dict[value] = index

#create a dictionary
#check if the compliment exists in the dictionary
# if yes, then return the complements's value and index
# if not, add the value and its index

# nums = [3,2,3]
# target=6
nums = [2,7,11,15] 
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6
print(Solution().twoSum(nums,target))