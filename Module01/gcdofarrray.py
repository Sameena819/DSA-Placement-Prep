class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        while b:
            a,b=b,a%b
        return a
obj=Solution()
nums=[2,5,6,9,10]
print(obj.findGCD(nums))