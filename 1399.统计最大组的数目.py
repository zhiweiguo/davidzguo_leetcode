#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    '''
    # 超时
    def countLargestGroup(self, n: int) -> int:
        count_dict = {}
        max_n = 0
        for i in range(n+1):
            num = i
            s = 0
            while num > 0:
                s += num%10
                num = num//10
            if s not in count_dict:
                count_dict[s] = 0
            count_dict[s] += 1
            max_n = max(max_n, s)
        
        max_count = 0
        for k,v in count_dict.items():
            if v == max_count:
                max_count += 1
        return max_count
    '''    
    def countLargestGroup(self, n: int) -> int:
        s = [0 for _ in range(n+1)]  # 记录每个数对应的和
        c = [0 for _ in range(37)]   # 记录每个和出现的次数，1 <= n <= 10^4 所以 最大的和为9999 -》36
        for i in range(1, n+1):
            s[i] = s[i // 10] + i % 10   # 因为循环是从小到大，所以可以直接使用 i//10出对应的和
            c[s[i]] += 1  # 更新次数
        max_n = max(c)   # 找到最大值，即出现次数最多的
        return sum(i==max_n for i in c)  # 返回并列最多的组数
        

# @lc code=end

