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

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diffs = {target - x for x in nums}
        numbers = set(nums).intersection(diffs)

        if len(numbers) == 1:
            result = list(numbers) * 2
        elif len(numbers) > 2:
            result = list(numbers - {target / 2})
        else:
            result = list(numbers)

        indicies = [0] * 2
        for i, n in enumerate(result):
            idx = nums.index(n)
            nums[idx] = None
            indicies[i] = idx

        return indicies


def main():
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([4, 3, 2], 6) == [0, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    main()
