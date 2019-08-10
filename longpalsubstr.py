def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    dp = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]
    longest = 0
    longest_pal = ''

    for substr_len in xrange(len(s)):
        left = 0
        right = left + substr_len
        while right < len(s):
            if s[left] == s[right] and (right - left < 2 or dp[left + 1][right - 1]):
                dp[left][right] = True
                if right - left + 1 > longest:
                    longest = right - left + 1
                    longest_pal = s[left:right+1]
            left, right = left + 1, right + 1
    return longest_pal
