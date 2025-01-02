
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        order_dict = dict()
        for i , (x, y) in enumerate(zip(s,t)):
            print(i, x, y)

            if x in order_dict.keys():
                if order_dict[x] != y:
                    return False
            else:
                if y in order_dict.values():
                    return False
            order_dict[x] = y
        return True
 

# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
s = "paper"
t = "title"
print(Solution().isIsomorphic(s,t))