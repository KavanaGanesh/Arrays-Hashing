# Algorithm: complexity is O(n)
# Usage of Counter(): pass one of the string into it
# ex: s='racecar', t = 'carrace'
# output of Counter(s) = {r:2,a:2,c:2,e:1} #idea: when counter[char] == 0 
# case1: if length(s and t) are not eqaul then return False
# case2: iterate through another string (t) using enumerate is best
    # if the char of t is presnt in s:
        # if count of that char == 0
            # return False
    # else: char of t is not present in s 
        # return False
    # decrement the count of char
# finally return True


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = Counter(s)

        for key, value in enumerate(t):
            if value not in s:
                return False
            if value in s:
                if count[value]==0:
                    return False
            count[value]-=1     
        return True
   

s = "aacc"
t = "ccac"     
# s = "aabbbb"
# t = "aaaabb"
# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
print(Solution().isAnagram(s,t))