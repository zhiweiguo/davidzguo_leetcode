#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    # 前两个list计算和，后两个list计算和
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums_dict = {}
        for n1 in nums1:
            for n2 in nums2:
                n = n1 + n2
                if n in sums_dict:
                    sums_dict[n] += 1
                else:
                    sums_dict[n] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                n = -(n3 + n4)
                if n in sums_dict:
                    count += sums_dict[n]
        return count 
        

    # 效率比较低，原因是后面的字典枚举又是o2的时间复杂度
    # def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:

    #     nums12 = {}
    #     nums34 = {}
    #     for n1 in nums1:
    #         for n2 in nums2:
    #             n = n1 + n2
    #             if n in nums12:
    #                 nums12[n] += 1
    #             else:
    #                 nums12[n] = 1
    #     for n3 in nums3:
    #         for n4 in nums4:
    #             n = n3 + n4
    #             if n in nums34:
    #                 nums34[n] += 1
    #             else:
    #                 nums34[n] = 1
    #     count = 0
    #     for k1, v1 in nums12.items():
    #         for k2, v2 in nums34.items():
    #             if (k1 + k2) == 0:
    #                 count += (v1 * v2)

    #     return count 



# @lc code=end


if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    sol =Solution()
    count = sol.fourSumCount(A,B,C,D)
