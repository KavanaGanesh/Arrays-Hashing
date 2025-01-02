# 1-1000thplace, 2-100thplace, 3-10place, 4-unitplace
# I need to pick the unit place first 
    # how do i get that? modulo division always gives remainder - 1234 % 10 = 4
    # Move that 4 from unit place to tenth place how? multiply 4 by 10
# I need to pick 10 place 
    # same but division by 100 (Inorder to replace by 10,100 everytime)

# Algorithm:
# res = 0
    # I=0-->  Modulo division first : 1234 % 10 = 4
    # integer division :1234/10 = 123
# * RES = 0 *10 + res = 4 (in unit place)
    # I=1--> Modulo division first : 123 % 10 = 3
    # integer division :123/10 = 12
# * # RES = 4*10 + 3 = 43(moved from unit to 10th place)
    # I=2--> Modulo division first : 12 % 10 = 2
    # integer division :12/10 = 1
# * # RES = 43 *10 + 2 = 432 (moved from 10th to 100th place)
    # I=3--> Modulo division first : 1 % 10 = 1
    # integer division :1/10 = 0
    # RES = 432 *10 + 1 = 4321 (moved from 100th to 1000th place)

# But any time if the modulo of the division doesnot fall within (-2^31  -x- 2^31-1) return 0

import math
class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2147483648  #(-2^31) remember i cannot store this entire value bcos of overflow
        max_val = 2147483647  #(2^31-1)
        result = 0

        while x:
            digit_value = int(math.fmod(x,10))
            #int(x%10)-the same logic with helper function
            x = int(x/10)
            if result < min_val // 10 or (result == min_val // 10 and digit_value < min_val % 10):
                return 0
            if result > max_val // 10 or (result == max_val // 10 and digit_value > max_val % 10):
                return 0
            result = (result * 10) + digit_value
        return result

x = 1234
# Output: 4321
# x = -1234
# Output: -4321
# x = 1234236467
# Output: 0
print(Solution().reverse(x))