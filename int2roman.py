class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        th = num // 1000 # find number of thousands
        out += "M" * th
        num = num - 1000 * th # find remainder
        hun = num // 100
        #soecial cases
        if hun == 4:
            out += "CD"
        elif hun == 9:
            out += "CM"
        elif hun >= 5:
            out += "D" + (hun - 5) * 'C'
        else:
            out += 'C' * hun
        num = num - 100 * hun
        #tens
        ten = num // 10
        if ten == 4:
            out += 'XL'
        elif ten == 9:
            out += 'XC'
        elif ten < 5:
            out += 'X' * ten
        else:
            out += 'L' + (ten - 5) * 'X'
        num = num - ten * 10
        #ones
        #special cases
        if num == 4:
            out += "IV"
        elif num == 9:
            out += "IX"
        elif num < 5:
            out += "I" * num
        else:
            out += "V" + (num - 5) * 'I'

        return out


