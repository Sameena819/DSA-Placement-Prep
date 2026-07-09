class Solution:
    def closestPalindrome(self, num):
        n = len(num)

        # If already a palindrome
        if num == num[::-1]:
            return num

        candidates = set()

        # Edge cases
        candidates.add(str(10 ** (n - 1) - 1))   # 999...
        candidates.add(str(10 ** n + 1))         # 100...001

        # First half of the number
        half = (n + 1) // 2
        prefix = int(num[:half])

        # Generate palindromes using prefix-1, prefix, prefix+1
        for p in [prefix - 1, prefix, prefix + 1]:
            if p < 0:
                continue
            s = str(p)

            if n % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[:-1][::-1]

            candidates.add(pal)

        original = int(num)
        ans = None
        mindiff = float('inf')

        for p in candidates:
            val = int(p)
            diff = abs(val - original)

            if diff < mindiff or (diff == mindiff and val < int(ans)):
                mindiff = diff
                ans = p

        return ans