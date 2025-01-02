
class Solution(object):
    def isHappy(self, n):
        new_set = set()
        while n!=1:
            if n in new_set:
                return False
            new_set.add(n)

            n = sum([int(x) **2  for x in str(n)])

        return True

# n = 19
'''Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1'''

n = 2
# Output: false

print(Solution().isHappy(n))