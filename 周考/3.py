import random
# 第三题
s=[]
a=0
c=0
for i in range(20):
    s+=str(random.choice(range(10)))
    # 随机数
for i in range(20):
    # 判断是否偶数
    if int(s[i])%2==0:
        s.sort()
        s.reverse()

print(s)