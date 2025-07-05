from math import floor, log10


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        exponent = floor(log10(x))
        while exponent > 0:
            if x//(10**exponent) == x%10:
                x -= (x//10**exponent)*(10**exponent) #remove first digit
                x //= 10 # remove last digit
                exponent -=  2
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(123))
    print(s.isPalindrome(121))
    print(s.isPalindrome(100))
    print(s.isPalindrome(12321))




