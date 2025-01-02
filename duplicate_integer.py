# Algorithm:Complexity is O(n)
# Create a hashmap: store the index as key and value as each element 
# Remember dictionary always store unique elements
# Loop through each element using enumerate- provides benefits index and value at the same time
    # check if the key is already availbale,
        # if yes - return True
    # check if the value is already availbale, 
        # if yes - return True
    # otherwise add to the dict as dict[index] = value
# finally return False if no duplicates found

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> List[int]:
        order_dict = dict()
        for x,y in enumerate(nums):
            if x in order_dict.keys():
                return True
            if y in order_dict.values():
                return True
            order_dict[x] = y
        return False
         

nums = [1, 2, 3, 3]
#Output: true if duplicates return True else False
nums = [1,2,3,4]
# output: False
print(Solution().hasDuplicate(nums))

# -------------------------------------------------------------------------------------------------
# using sets - o(n) - time, o(1) - space
# from typing import List
# data = [1, 2, 3, 2, 5, 1, 4]
 

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> List[int]:
#         list_set = set()
#         duplicates = set()
#         for item in data:
#             if item in list_set:
#                 duplicates.add(item)
#             else:
#                 list_set.add(item)
#         return duplicates
                
# print(Solution().hasDuplicate(data))