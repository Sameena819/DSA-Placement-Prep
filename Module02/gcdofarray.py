from math import gcd
class Solution:
    def gcd(self, n, arr):
        ans=arr[0]
        for i in range(1,n):
            ans=gcd(ans,arr[i])
        return ans
obj = Solution()

print(obj.gcd(3, [1, 2, 3]))      
print(obj.gcd(4, [2, 4, 6, 8]))   