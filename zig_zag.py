class Solution:
    @staticmethod
    def tr_join(s1: str, s2: str) -> str:
        assert (0 <= len(s1) - len(s2) <= 1)

        out = "".join("".join(v) for v in zip(s1, s2))
        if len(s1) == len(s2):
            return out
        else:
            return out + s1[-1]

    def convert(self, s: str, numRows: int) -> str:
        rows =[]
        if numRows == 1:
            return s
        jmp = 2*numRows -2
        for ii in range(numRows):
            if (ii == 0) or (ii == numRows - 1):
                rows.append(s[ii::jmp])
            else:
                rows.append(self.tr_join(s[ii::jmp], s[jmp-ii::jmp]))
        return "".join(rows)


if __name__ == "__main__":
    s1 = "PAYPALISHIRING"
    soln = Solution()
    print(soln.convert(s1, 3))
    print(soln.convert(s1, 4))

