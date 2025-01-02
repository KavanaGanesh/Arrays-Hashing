from typing import List

# '''Mysolution passes the testcases but needs to be optimized'''
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         new_string = []
#         for i in range(len(strs)):
#             if strs[0][i] == strs[1][i] == strs[2][i]:
#                 new_string.append(strs[0][i])
#         return "".join(new_string)
    
# neetcode
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end_res = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return end_res
            end_res += strs[0][i]
        return end_res

 
# strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))