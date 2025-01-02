# Algorithm: to return the length of the longest consecutive sequence
# create a set to remove duplicate values: 
    # the output will be in ascending order with no duplicates
# pick each number from nums
# check if the previous number exists in the set : 
    # if yes: then the current no is not the start of the longest sequence
    # if no: the current number is the start of the sequence, keep its length to be 1 and the number is the current number
        # now check if the current number + 1 exists in the set with the while loop:
            #  if yes: then keep checking next element in the set with updating the length
        # update the length - max(longest,currentnumber_length)
# return the longest



from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for number in nums:
            if number-1 not in numset:# check if it is the start of the sequence that is 
                # if the number dosnot have a left neighbor
                current_length = 1
                current_number = number

                while current_number + 1 in numset:
                    current_number = current_number + 1
                    current_length = current_length + 1


                longest = max(longest, current_length)
        return longest




nums = [2,20,4,10,3,4,5]
# nums = [0,3,2,5,4,6,1,1]
print(Solution().longestConsecutive(nums))