# from typing import List

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return str(s)
#         s_split = strs.split(" ")
#         return s_split

#     def decode(self, s: str) -> List[str]:
#         if len(s) == 0:
#             return list(s)
#         s_split = s.split(" ")
#         return s_split


# # strs = ["neet","code","love","you"]
# strs = []

# encode_result = Solution().encode(strs)
# # decode_result = Solution().decode(encode_result)
# print(encode_result)
# print(decode_result)

# THE ABOVE SOLUTION DOESNOT SATISFY WHEN GIVEN AN EMPTY STRING
# ----------------------------------------------------------------------------

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        strs_res = ""
        for s in strs:
            strs_res += str(len(s)) + '*' + s
        return strs_res

    def decode(self, s: str) -> List[str]:
        list_res = []
        i = 0

        while i<len(s):
            j = i

            while s[j] != '*': # this loop is for each character "5*hello"
                j+=1
            length = int(s[i:j]) # this gives the value of the integer = 5
            list_res.append(s[j+1 : j+1+length]) # here append the word "hello"
            i = j+1+length # here pointer is at another numeric "5*world"

        return list_res



strs = ["hello", "world", "leetcode", "example"]
# strs = []

encode_result = Solution().encode(strs)
decode_result = Solution().decode(encode_result)
print(encode_result)
print(decode_result)