# The find() method returns the index of the first occurrence of the specified value.
# this particularly works for strings only


# The find() method returns -1 if the value is not found.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

haystack = "sadbutsad"
needle = "sad"
# haystack = "leetcode" 
# needle = "leeto"      


print(Solution().strStr(haystack,needle))