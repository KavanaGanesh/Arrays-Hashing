# 1)split and get the last word of the sentence - return value of the split is list[words]
# 2)call the length of the last word

# space and time complexities both are O(n) as it is goign to create the substring.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return (len(s.split( )[-1]))


s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))
        