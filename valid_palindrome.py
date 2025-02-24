# Algorithm: 
# 1) create an empty string
# 2) First check if each character is is alnum : that is it can alphabets or number (case insensitive)
# 3) add each character to the empty string created
# 4) now compare both of the string by the lower and reversing 
# 5) return True if match else False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str = new_str + c.lower()
        return True if new_str == new_str[::-1] else False
        

s = "Was it a car or a cat I saw?"
print(Solution().isPalindrome(s))