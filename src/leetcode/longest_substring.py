class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = []
        lon_tmp = []
        for letter in s:
            if letter not in tmp:
                tmp.append(letter)
            else:
                if len(tmp) > len(lon_tmp):
                    lon_tmp = tmp
                tmp = tmp[tmp.index(letter) + 1 :]
                tmp.append(letter)
        if len(tmp) > len(lon_tmp):
            lon_tmp = tmp
        return len(lon_tmp)

    @classmethod
    def factory(cls) -> "Solution":
        return Solution()
