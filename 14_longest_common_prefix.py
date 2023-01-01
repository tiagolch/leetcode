'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "". 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

https://leetcode.com/problems/longest-common-prefix/

'''
from typing import List
import pytest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            while word.startswith(prefix) == False:
                prefix = prefix[:-1]
        return prefix

strs_ = ["flower","flow","flight"]
Solution().longestCommonPrefix(strs_)

@pytest.mark.parametrize('strs, result', [
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], ''),
    (["flower","flow","flight","fx"], 'f'),
    (["flower","flow","flight","fx", "tiago", "luiz"], ''),
])
def test_longest_common_prefix(strs, result):
    assert Solution().longestCommonPrefix(strs) == result