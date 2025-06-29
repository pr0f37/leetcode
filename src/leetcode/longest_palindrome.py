class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for idx, letter in enumerate(s):
            tmp_palindrome = letter
            l_idx = idx - 1
            r_idx = idx + 1
            while r_idx < len(s) and s[r_idx] == letter:
                tmp_palindrome = tmp_palindrome + s[r_idx]
                r_idx += 1
            while l_idx >= 0 and r_idx < len(s) and s[l_idx] == s[r_idx]:
                tmp_palindrome = s[l_idx] + tmp_palindrome + s[r_idx]
                l_idx -= 1
                r_idx += 1
            if len(tmp_palindrome) > len(longest_palindrome):
                longest_palindrome = tmp_palindrome
            if len(longest_palindrome) >= (len(s) - idx) * 2:
                break
        return longest_palindrome
