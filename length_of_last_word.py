class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return (len(s.split( )[-1]))


s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))
        