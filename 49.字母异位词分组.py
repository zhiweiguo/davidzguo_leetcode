#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
import collections
from typing import Collection


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            groups_dict[tuple(counts)].append(s)
        return list(groups_dict.values())

    # # 超时
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     groups = []
    #     for s in strs:
    #         find_anagram = False
    #         for i in range(len(groups)):
    #             if self.isAnagram(s, groups[i][-1]):
    #                 groups[i].append(s)
    #                 find_anagram = True
    #                 break
    #         if not find_anagram:
    #             groups.append([s])
    #     return groups

    # def isAnagram(self, s: str, t: str) -> bool:
    #     char_count = [0] * 26
    #     for c in s:
    #         char_count[ord(c)-ord('a')] += 1
    #     for c in t:
    #         char_count[ord(c)-ord('a')] -= 1
    #     for n in char_count:
    #         if n != 0:
    #             return False
    #     return True        
# @lc code=end

