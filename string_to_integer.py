import re


class Solution:
    max_val = 2 ** 31 - 1
    min_val = -2 ** 31


    def myAtoi(self, s: str) -> int:
        is_neg = False
        expr = re.compile(r"[+-]?\d+")
        s = s.strip()
        out_match = expr.match(s)
        if not out_match:
            return 0

        outs = s[:out_match.span()[1]]
        if outs.startswith('-'):
            is_neg = True
            outs = outs[1:]
        outs = outs.lstrip('0')
        if not outs:
            return 0
        out =int(outs)
        if is_neg:
            out = out * -1

        if out > self.max_val:
            return self.max_val
        if out < self.min_val:
            return self.min_val
        return out
if __name__ == "__main__":
    s1 = Solution()
    print(s1.myAtoi("42"))
    print(s1.myAtoi("-42"))
    print(s1.myAtoi("042"))
    print(s1.myAtoi("   -042"))
    print(s1.myAtoi("123456789101112131415"))
    print(s1.myAtoi("-123456789101112131415"))
    print(s1.myAtoi("0-d"))