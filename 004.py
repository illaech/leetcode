"""4. Median of Two Sorted Arrays

Description:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log(m+n)).

    Example 1:
        Input: nums1 = [1, 3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1, 2, 3] and median is 2.

    Example 2:
        Input: nums1 = [1, 2], nums2 = [3, 4]
        Output: 2.50000
        Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.

    Constraints:
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -10⁶ <= nums1[i], nums2[i] <= 10⁶

Results:
    Runtime: 137 ms, faster than 47.98% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.2 MB, less than 87.44% of Python3 online submissions for Median of Two Sorted Arrays.
"""


from typing import Literal


def get_or_inf(seq: list[int], idx: int, sign: Literal[1, -1] = 1) -> int | float:
    """Get element from array or return infinity of chosen sign.

    Args:
        seq: array to get element from
        idx: index of element
        sign: sign of infinity, either 1 or -1

    Returns:
        int | float: element from array or infinity
    """

    try:
        return seq[idx]
    except IndexError:
        return sign * float("inf")


def solve(a: list[int], b: list[int]) -> int | float:
    """Retrieve median of sorted arrays.

    Median of array is either middle element or average of two middle elements. To avoid merging arrays into one, the
    logical trick can be used: all is needed is to split arrays in such way that resulting middle elements would be
    on borders of partitions. For example, if the first array is [1, 2, 6] and the second is [3, 7], split would
    look like [1, 2] | [6] and [3] | [7]. Thus, the last element of the left partition of the first array must be
    less or equal to the first element of the right partition of the second array, and the last element of the left
    partition of the second array must be less or equal to the first element of the right partition of the first array.
    Let's make some variables: α and β are the given arrays of size m and n; αₗ, αᵣ, βₗ, βᵣ are the partitions of the
    arrays α and β; α₁ = αₗ[-1], α₂ = αᵣ[0], β₁ = βₗ[-1], β₂ = βᵣ[0] are border elements; and z = m + n — total number
    of elements in both arrays. So, the goal here is to find such split position, that α₁ ≤ β₂ and β₁ ≤ α₂. After
    finding such position, all border elements are medium-esque: every element inside left partitions is less or equal
    to any element of right partitions. So, all that is needed is to find the real "medium", and this search vary on
    oddness of total number of elements z. If z is odd, the result is max(α₁, β₁), otherwise the result is equal to
    average(max(α₁, β₁), min(α₂, β₂)). For that little example result is max(2, 3) == 3.

    To find the correct split position the binary search is used. Starting at the middle of α, there's a check for
    needed condition: α₁ ≤ β₂ and β₁ ≤ α₂. If the first half is false, then the search is too much on the right side
    and needed to be shifted to the left, so the ending point is moved to the previous position - 1. If the latter half
    is false, then the search is too much on the left, so the starting point is moved to the previous position + 1.
    It goes on until the needed condition is satisfied.

    Split position in the α array is calculating simply: posₐ = (start + end) // 2. Split position in the β array is
    more complex. It is coming from our goal: median is the middle element, so we need to split both of our arrays
    combined into two halfs with the same number of elements, so z / 2 is such a number. Due to z might be odd let's
    add 1 and round it down: (z + 1) // 2. Thus, moving to separate positions for each array:
    posₐ + posᵦ = (z + 1) // 2, and finally posᵦ = (z + 1) // 2 - posₐ.

    Because it is possible to have all of the elements from array α greater than all of the elements of array β,
    posₐ would be equal to 0 and αₗ would be empty. To get through this (and similar) situation it's needed to give
    two more rules:
        - if left partition is empty, its last element is treated as -inf,
        - if right partition is empty, its first element is threated as +inf.


    Args:
        a: shortest array
        b: other array

    Result:
        int | float: median of arrays
    """

    # calc once
    m, n = len(a), len(b)
    k, odd = (m + n + 1) // 2, (m + n) % 2 == 1

    # definitions
    start, end = 0, m
    a_left, a_right = [], []
    b_left, b_right = [], []

    while True:
        pos_a = (start + end) // 2  # split of α array
        pos_b = k - pos_a  # split of β array

        a_left, a_right = a[:pos_a], a[pos_a:]
        b_left, b_right = b[:pos_b], b[pos_b:]

        # IndexErrors :\
        a1, b2 = get_or_inf(a_left, -1, -1), get_or_inf(b_right, 0)

        if a1 <= b2:
            a2, b1 = get_or_inf(a_right, 0), get_or_inf(b_left, -1, -1)

            if b1 <= a2:
                return max(a1, b1) if odd else (max(a1, b1) + min(a2, b2)) / 2.0
            start = pos_a + 1
        else:
            end = pos_a - 1


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # find the shortest one of given arrays to speed up the binary search
        if len(nums1) > len(nums2):
            return solve(nums2, nums1)
        return solve(nums1, nums2)


def main():
    sol = Solution()

    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([1, 2], [3, 4, 5]) == 3
    assert sol.findMedianSortedArrays([1, 2, 6], [3, 7]) == 3


if __name__ == "__main__":
    main()
