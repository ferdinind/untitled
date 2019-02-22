list=[2,5,6,3,6,5,41,5,21]
list1=[]
for i in range(len(list)):
    # 循环遍历追加到新数组
    list1.append(list[i])
print(list)
# 反向输出
list1.reverse()
print(list1)