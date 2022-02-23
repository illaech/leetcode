"""2. Add Two Numbers

Difficulty:
    Medium.

Link:
    https://leetcode.com/problems/add-two-numbers

Description:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
        2 → 4 → 3
        5 → 6 → 4
        -----------
        7 → 0 → 8

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

    Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]

    Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]


    Constraints:
        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

Results:
    Runtime: 76 ms, faster than 71.98% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Add Two Numbers.
"""


# Defition for singly-linked list from problem description.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_to_int(ln: ListNode) -> int:
    """Convert ListNode sequence into integer"""

    # listnode starts with units, then goes up to tens, hundreds, etc.
    num, exp = 0, 0
    while ln:
        num += ln.val * 10**exp
        exp += 1
        ln = ln.next

    return num


def convert_to_listnode(num: int) -> ListNode:
    """Convert integer into ListNode sequence"""

    # returned ListNode must be ListNode of units, so recursion is started from units
    if num // 10 == 0:
        return ListNode(num)
    return ListNode(num % 10, convert_to_listnode(num // 10))


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        return convert_to_listnode(convert_to_int(l1) + convert_to_int(l2))


def main():
    sol = Solution()

    def ln(lst: list[int]) -> ListNode:
        fst = ListNode(lst[0])
        iterator = fst
        for i in lst[1:]:
            y = ListNode(i)
            iterator.next = y
            iterator = y
        return fst

    assert convert_to_int(sol.addTwoNumbers(ln([2, 4, 3]), ln([5, 6, 4]))) == 807
    assert convert_to_int(sol.addTwoNumbers(ln([0]), ln([0]))) == 0
    assert convert_to_int(sol.addTwoNumbers(ln([9, 9, 9, 9, 9, 9, 9]), ln([9, 9, 9, 9]))) == 10009998


if __name__ == "__main__":
    main()
