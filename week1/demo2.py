# 编写程序，生成一个包含50个随机整数的列表
# ，随机整数的范围是从-10到10，
# 然后将列表中所有的正数存为一个新的子列表，
# 负数存为另一个新的子列表。

import random
var=[]
zheng=[]
fu=[]

for i in range(50):
    var.append(random.choice(range(-10,10)))
    if var[i]>0:
        zheng.append(var[i])
    else:
        fu.append(var[i])
print(var)
print(zheng)
print(fu)