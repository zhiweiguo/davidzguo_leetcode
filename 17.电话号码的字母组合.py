#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def __init__(self):
        self.answers = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:   
        self.answers = []
        if not digits:
            return self.answers
        path = ''
        self.backtracking(digits, path, 0)
        return self.answers
    
    def backtracking(self, digits, path, start_idx):
        if start_idx == len(digits):
            self.answers.append(path)
            return
        letters = self.letter_map[digits[start_idx]]
        for letter in letters:
            self.backtracking(digits, path+letter, start_idx+1)

    

# @lc code=end

