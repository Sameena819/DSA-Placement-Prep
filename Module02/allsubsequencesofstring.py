class Solution:
    def AllPossibleStrings(self, s):
        ans = []

        def solve(i, curr):
            if i == len(s):
                ans.append(curr)
                return

            # Include current character
            solve(i + 1, curr + s[i])

            # Exclude current character
            solve(i + 1, curr)

        solve(0, "")
        ans.sort()
        return ans