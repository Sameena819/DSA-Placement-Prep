class Solution:
    def binaryToDecimal(self, b):
        ans = 0
        for digit in b:
            ans = ans * 2 + int(digit)
        return ans

obj = Solution()
print(obj.binaryToDecimal("1001"))