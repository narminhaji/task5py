
class MyClass:
    def __init__(self, *nums):
        self.mylist = list(nums)
    def Sum(self, target):
        myset = {}
        for i, num in enumerate(self.mylist):
            dif = target - num
            if dif in myset:
                return [myset[dif], i]
            myset[num] = i
        return -1
myclass = MyClass(24, 55, 2, 4, 49, 17, 13, 3)
print(myclass.Sum(5)) 