# 编写程序，生成一个包含20个随机整数的列表，
# 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
# 奇数下标的元素不变。
import random
var=[]

for i in range(20):
    var.append(random.choice(range(100)))
    print(var[i])
var[::2]=sorted(var[::2],reverse=True)
print(var)
print(var.__len__())
