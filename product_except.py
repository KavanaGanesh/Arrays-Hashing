# Algorithm:given list of integers, requirement is return output list with products except the self.
# input = [1,2,4,6], output = [48,24,12,8]
# keep prefix list = which is the multiplication of the previous value(i[0] = 1, i[1] = i[0], i[2] = i[0] * i[1], i[3] = [0]*i[1]*[2] (moving left to right)
# keep postfix list = which is the multiplication of the previous value(i[-1] = 1, i[-2] = i[-1], i[-3] = i[-2]*i[-1], i[-4] = i[-3]*i[-2]*i[-1])
# but keeping 2 lists -  space complexity will be O(n)
# lets keep the same logic of multiplication but instead use inplace modification on the input array
# so res_output = [1]*len(input_array)
# need 2 pointers
        # left -  one to move from left for prefixlist calculation
            # nums[i] = [1,2,4,6], left = 1
            # res = [1,1,1,1]
            # loop through each element to update the res and left
            # res[i] = left and left = left *nums[i] -  refer book for analysis
        # right - move fromn right for posfix calculation
            # nums[i] = [1,2,4,6], right  = 1
            # res = [1,1,2,8] -> res list is updated from prefixlist calculation
            # res[i] = res[i]*right
            # right = right * nums[i]


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_output = [1] *len(nums)
        left=1
        
        for i in range(len(nums)):
            res_output[i] = left
            left = left*nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res_output[i] = res_output[i]*right
            right = right*nums[i]

        return res_output

print(Solution().productExceptSelf([1,2,3,4]))
       