from collections import defaultdict


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d = defaultdict(int)
        out = []
        odd = ''
        for ch in s:
            d[ch] += 1
        for ii, ch in enumerate(sorted(d.keys())):
            if d[ch] % 2 == 0:
                out.append(ch*(d[ch] // 2))
            else:
                if odd:
                    raise ValueError("No Palindrome")
                else:
                    out.append(ch * (d[ch] // 2))
                    odd = ch

        out = "".join(out)
        return out + odd + out[-1::-1]


if __name__ == "__main__":
    sol = Solution()
    res = sol.smallestPalindrome("bbbaa")
    print(res)
    res = sol.smallestPalindrome("aaaccdd")
    print(res)
    print(sol.smallestPalindrome("inini"))
