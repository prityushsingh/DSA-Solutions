class Solution(object):
    def processStr(self, s):
        res = []
        for c in s:
            if c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res += res[:]
            elif c == "%":
                left = 0
                right = len(res) - 1
                while left < right:
                    res[left] , res[right] = res[right] , res[left]
                    left += 1
                    right -= 1
            else:
                res.append(c)
        return "".join(res)


#Time complexity : O(N²) in the worst case due to repeated string concatenation and copying
#Space complexity : O(N)
