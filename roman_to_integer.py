class Solution:
    def romanToInt(self, s: str) -> int:
        # simple logic: compare first and next element, if greater add the element, else subtract
        dict_roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        prev_value = 0
        for i in range(len(s)):
            if i+1 <len(s) and dict_roman[s[i]] < dict_roman[s[i+1]]:
                prev_value -= dict_roman[s[i]]
            else:
                prev_value += dict_roman[s[i]]
        return prev_value




# s = "III"
s = "LVIII"
# s = "MCMXCIV"
print(Solution().romanToInt(s))

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


