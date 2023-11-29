""" 
    有两种方法做: 

    (1) 用两个双向队列
        叶师傅 https://leetcode.cn/problems/design-front-middle-back-queue/solutions/2544779/gong-shui-san-xie-qing-xi-gao-xiao-de-qu-o0eq/?envType=daily-question&envId=2023-11-28
        灵神 https://leetcode.cn/problems/design-front-middle-back-queue/solutions/2544784/tu-jie-liang-ge-shuang-duan-dui-lie-jian-43pr/?envType=daily-question&envId=2023-11-28

    (2) 用一个双向队列 + 中间位置的指针
        叶师傅 https://leetcode.cn/problems/design-front-middle-back-queue/solutions/2544779/gong-shui-san-xie-qing-xi-gao-xiao-de-qu-o0eq/?envType=daily-question&envId=2023-11-28
        零神 https://leetcode.cn/problems/design-front-middle-back-queue/solutions/502014/she-ji-qian-zhong-hou-dui-lie-by-zerotrac2/?envType=daily-question&envId=2023-11-28
    
    参考资料: 
        python的__slots__属性 https://zhuanlan.zhihu.com/p/578699693
            
    疑问: 
        都规定了 len(right) - len(left) = 1 
        为什么啊? 是不是只是习惯的问题，因为奇数总要多一个出来。

    闪光点:
        这里用 balance 和 "分类讨论"数学思想 解决了大部分的问题。
""" 

from collections import deque


class FrontMiddleBackQueue:
    __slots__ = 'left', 'right'

    def __init__(self):
        self.left = deque() 
        self.right = deque()

    def balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1: 
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:
            return -1 
        val = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return val 

    def popMiddle(self) -> int:
        if not self.right:
            return -1 
        if len(self.left) == len(self.right):
            return self.left.pop()
        return self.right.popleft()

    def popBack(self) -> int:
        if not self.right:
            return -1 
        val = self.right.pop()
        self.balance()
        return val 



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

