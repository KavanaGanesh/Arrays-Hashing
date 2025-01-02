# The find() method finds the first occurrence of the specified value.

# The find() method returns -1 if the value is not found.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode" 
needle = "leeto"


print(Solution().strStr(haystack,needle))