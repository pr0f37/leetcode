from leetcode.longest_substring import Solution


def test_complicated():
    assert Solution().lengthOfLongestSubstring("aabaab!bb") == 3


def test_factory():
    assert Solution.factory().lengthOfLongestSubstring("aabaab!bb") == 3
