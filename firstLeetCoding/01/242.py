from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1

        for char in t:
            char_dict[char] -= 1

        for char in char_dict:
            if char_dict[char] != 0:
                return False
        return True


s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
