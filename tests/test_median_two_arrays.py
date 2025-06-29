from leetcode.median_two_arrays import Solution


def test_findMedianSortedArrays():
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0


def test_findMedianSortedArrays_2():
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
