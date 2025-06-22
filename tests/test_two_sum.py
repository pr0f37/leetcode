from leetcode.two_sum import Solution


def test_one():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


if __name__ == "__main__":
    test_one()
    print("All tests passed!")
