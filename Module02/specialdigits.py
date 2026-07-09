class Solution:
    MOD = 10**9 + 7

    def bestNumbers(self, n, a, b, c, d):
        mod = self.MOD

        def valid(x):
            while x > 0:
                t = x % 10
                if t == c or t == d:
                    return True
                x //= 10
            return False

        if a == b:
            return 1 if valid(n * a) else 0

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], mod - 2, mod)

        for i in range(n - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % mod

        ans = 0

        for i in range(n + 1):
            s = i * a + (n - i) * b
            if valid(s):
                ways = fact[n]
                ways = ways * invfact[i] % mod
                ways = ways * invfact[n - i] % mod
                ans = (ans + ways) % mod

        return ans