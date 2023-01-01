'''
You are given a string s of even length. Split this string into two halves of equal lengths, 
and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

https://leetcode.com/problems/determine-if-string-halves-are-alike/
'''

import pytest


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ('a', 'e', 'i', 'o', 'u')
        a, b = '', ''

        def countVowel(string : str) -> int:
            count = 0
            for i in string:
                if i.lower() in vowel:
                    count += 1          
            return count

        count_a, count_b = 0, 0
        a = s[:len(s)//2]
        b = s[len(s)//2:]

        count_a = countVowel(a)
        count_b = countVowel(b)

        if count_a == count_b:
            result = True
        else:
            result = False      

        return result



@pytest.mark.parametrize("string, result", [
    ('testes', True),
    ('aaaaba', False),
])

def test_halves_are_alike(string, result):
    assert Solution().halvesAreAlike(string) == result
