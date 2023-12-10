"""

    第一感觉就是“动态规划”，结果看了答案，原来还不止啊，还有“排序”。
    所以想问题要全面，想好下一步。

"""

from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        n = n + 1 
        rides = sorted(rides, key=lambda r: r[0])
        f = [0] * n
        curr_passenger = 0 
        for i in range(1, n):
            curr_start = rides[curr_passenger][0]
            # curr_end = rides[curr_passenger][1]
            curr_tip = rides[curr_passenger][2]
            if curr_start == i: 
                f[i] = f[i-curr_start] + curr_tip
            else: 
                f[i] = f[i-1]  

