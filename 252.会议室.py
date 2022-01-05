# leetcode 252, 253题，会议室相关为题
# 题解：https://mp.weixin.qq.com/s/YVqd4J1GVnh25FKk8FUYzA
# 描述：给你输入若干形如[begin, end]的区间，代表若干会议的开始时间和结束时间，请你计算至少需要申请多少间会议室。
# 比如给你输入meetings = [[0,30],[5,10],[15,20]]，算法应该返回 2，因为后两个会议和第一个会议时间是冲突的，至少申请两个会议室才能让所有会议顺利进行。
# 技能点： 差分数组， 双指针
def minMeetingRooms(meetings):
    starts = []
    ends = []
    for item in meetings:
        starts.append(item[0])
        ends.append(item[1])
    starts.sort()
    ends.sort()
    count = 0
    max_count = 0
    i = 0
    j = 0
    while i < len(meetings) and j < len(meetings):
        if starts[i] <= ends[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        max_count = max(count, max_count)
    return max_count