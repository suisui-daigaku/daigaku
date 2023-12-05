"""
差分数组: 
    https://leetcode.cn/problems/car-pooling/solutions/2546591/pin-che-by-leetcode-solution-scp6/?envType=daily-question&envId=2023-12-02
    构建 “差分数组”,  数组 count 来记录每一个位置时的乘客数量。

直接模拟:
    ... 
"""


from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        to_max = max(t[2] for t in trips)
        diff = [0] * (to_max + 1)
        for num_i, from_i, to_i in trips:
            diff[from_i] += num_i
            diff[to_i] -= num_i
        
        count = 0                       # count = [0] * len(diff)
        for i in range(to_max + 1): 
            count += diff[i]            # count[i] = count[i-1] + diff[i]
            if count > capacity:
                return False
        return True


