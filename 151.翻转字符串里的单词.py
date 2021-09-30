#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''    # 初始化
        right = len(s) - 1
        while right >=0:
            if s[right] == ' ':     # 为空时左移
                right -= 1
                continue
            else: 
                left = right    # 不为空时right为当前要找的单词的右边界
                while left >= 0 and s[left] != ' ': # 找左边界
                    left -= 1
                res += s[left+1:right+1] + ' '  # 后面加空格
                right = left -1

        return res[:-1]   # 删除最后一个多余的空格

# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    s = "the sky is blue"
    res = sol.reverseWords(s)
    print(res)

