"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]


Constraints:
    2 <= nums.length <= 10⁴
    -10⁹ <= nums[i] <= 10⁹
    -10⁹ <= target <= 10⁹
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?
"""


def solve(nums: list[int], target) -> list[int]:
    diffs = {target - x for x in nums}
    numbers = set(nums).intersection(diffs)

    # Due to the last constrain, `numbers` can only be 1 to 3 items long:
    #   1 — if result is `target / 2`,
    #   2 — two different numbers,
    #   3 — two different numbers and `target / 2`.
    # Thus, cases 1 and 3 must be slightly corrected to get the expected result.

    if len(numbers) == 1:
        # duplicate number
        return list(numbers) * 2
    if len(numbers) > 2:
        # exclude `target / 2`
        return list(numbers - {target / 2})
    return list(numbers)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = solve(nums, target)

        indices = [0] * 2  # makes a list only two items long it terms of used memory
        for i, n in enumerate(numbers):
            idx = nums.index(n)
            nums[idx] = None  # exclude used index from original array (for `target / 2` situation)
            indices[i] = idx

        # Because I don't shuffle or sort any lists, indices are in ascending order, so just return them as-is.
        return indices


def main():
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([4, 3, 2], 6) == [0, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    main()
