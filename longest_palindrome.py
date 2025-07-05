def is_palindrome(s: str) -> bool:
    length = len(s)
    if length%2 != 0:
        return s[:(length-1)//2] == s[length-1:(length-1)//2:-1]
    return s[:length//2] == s[length-1:(length-1)//2:-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for i in range(length-1, 0, -1):
            for j in range(0,length - i):
                if is_palindrome(s[j:j+i+1]):
                    return s[j:j+i+1]
        return s[0]


if __name__ == '__main__':
     print(Solution().longestPalindrome("babad"))
     print(Solution().longestPalindrome("cbbd"))
     print(Solution().longestPalindrome("aab"))
     print(Solution().longestPalindrome("aabbcbbaa"))