import random
#调用随机random包
var=""
z=[]
f=[]
for i in range(50):
    # 循环获取数值
    var=str(random.choice(range(-10,11)))
    #获取随机数
    if int(var)>0:
        # 判断正负
        z+=var
    else:
        f+=var
print(z)
print(f)