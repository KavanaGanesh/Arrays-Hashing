# 1) take the first word flight = iterate for the length of the word
# 2) now compare the letter "f" with firstword, then second word , and then 3rd word : if all the 3 words have f 
# 3) append to the new string created
# 4) similarly compare for all the letters for the length of the first word
# 5) print the end result

# complexities space = O(n)= length of the string
            # time = outer loop with in operator O(n) * Inner loop with in operator O(m) = O(n*m)

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
                # if word[i] != strs[0][i]:
                if i == len(word) or word[i] != strs[0][i]:
                    return end_res
            end_res += strs[0][i]
        return end_res

 
strs = ["dog","racecar","car"]
# strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))