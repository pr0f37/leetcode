from leetcode.add_two_numbers import ListNode, Solution


def test_simple():
    one = ListNode(1, ListNode(2, None))
    two = ListNode(2, ListNode(2, None))
    res = Solution().addTwoNumbers(one, two)
    assert res.val == 3
    assert res.next.val == 4


def test_complicated():
    one = ListNode(9, ListNode(2, None))
    two = ListNode(2, ListNode(2, None))
    res = Solution().addTwoNumbers(one, two)
    assert res.val == 1
    assert res.next.val == 5


def test_complicated_2():
    one = ListNode(9, ListNode(9, None))
    two = ListNode(2, ListNode(2, None))
    res = Solution().addTwoNumbers(one, two)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 1


if __name__ == "__main__":
    one = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    two = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    res = Solution().addTwoNumbers(one, two)
    assert res.val == 3
    assert res.next.val == 4
