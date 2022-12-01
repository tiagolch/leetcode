'''

Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.
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
'''

import pytest


def two_sum(self, nums: List[int], target: int) -> List[int]:
    pass


@pytest.mark.parametrize("nums, target, result", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 7, 11, 15, 3, 8], 26, [2, 3]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([2, 7, 11, 15], 3, []),
    # Casos de teste onde index é não consecutivo
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([3, 2, 3], 6, [0, 2]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([150, 24, 79, 50, 88, 345, 3], 200, [0, 3])
])

def test_two_sum(nums, target, result):
    assert two_sum(nums, target) == result
